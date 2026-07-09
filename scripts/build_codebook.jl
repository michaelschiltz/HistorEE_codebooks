#!/usr/bin/env julia
# Generate codebook.md for every dataset from its datapackage.json.
#
# Julia equivalent of build_codebook.py. One source of truth: the schema; the
# codebook is compiled, never hand-edited. Depends only on JSON.jl (Julia ships
# no JSON parser in the standard library); the CSV coverage count is done with a
# small quote-aware parser so no CSV package is required.
#
# Choose ONE generator for the repo — Python OR Julia — not both. Two generators
# that must be kept in sync is exactly the maintenance liability the project is
# trying to avoid. See CONTRIBUTING.md.
#
# Usage:
#   julia scripts/build_codebook.jl          # regenerate all
#   julia scripts/build_codebook.jl <dir>    # regenerate one dataset folder

import JSON

const ROOT = normpath(joinpath(@__DIR__, ".."))
const DATASETS = joinpath(ROOT, "datasets")

"Parse one CSV line into fields, honouring double-quoted fields and \"\" escapes."
function parse_csv_line(line::AbstractString)
    fields = String[]
    buf = IOBuffer()
    inquote = false
    i = firstindex(line)
    while i <= lastindex(line)
        c = line[i]
        if inquote
            if c == '"'
                if i < lastindex(line) && line[nextind(line, i)] == '"'
                    write(buf, '"'); i = nextind(line, i)
                else
                    inquote = false
                end
            else
                write(buf, c)
            end
        else
            if c == '"'
                inquote = true
            elseif c == ','
                push!(fields, String(take!(buf)))
            else
                write(buf, c)
            end
        end
        i = nextind(line, i)
    end
    push!(fields, String(take!(buf)))
    return fields
end

"Return (n_rows, present::Dict) counting non-missing cells per field."
function coverage(csv_path, fields, missing_tokens)
    present = Dict{String,Int}(f["name"] => 0 for f in fields)
    isfile(csv_path) || return (0, present)
    miss = Set(String.(missing_tokens))
    lines = readlines(csv_path)
    isempty(lines) && return (0, present)
    header = parse_csv_line(lines[1])
    idx = Dict(name => k for (k, name) in enumerate(header))
    n = 0
    for line in lines[2:end]
        isempty(strip(line)) && continue
        n += 1
        cells = parse_csv_line(line)
        for f in fields
            k = get(idx, f["name"], 0)
            k == 0 && continue
            v = k <= length(cells) ? strip(cells[k]) : ""
            if v != "" && !(v in miss)
                present[f["name"]] += 1
            end
        end
    end
    return (n, present)
end

md_escape(s) = replace(replace(something(s, ""), "|" => "\\|"), "\n" => " ")

function build(dataset_dir)
    dp = JSON.parsefile(joinpath(dataset_dir, "datapackage.json"))
    res = dp["resources"][1]
    schema = res["schema"]
    fields = schema["fields"]
    missing_tokens = get(schema, "missingValues", [""])
    csv_path = joinpath(dataset_dir, res["path"])
    n_rows, present = coverage(csv_path, fields, missing_tokens)

    lic = join([get(l, "name", "") for l in get(dp, "licenses", [])], ", ")
    lic = isempty(lic) ? "—" : lic
    contribs = join([string(get(c, "title", ""), " (", get(c, "role", ""), ")")
                     for c in get(dp, "contributors", [])], ", ")
    contribs = isempty(contribs) ? "—" : contribs

    io = IOBuffer()
    w(s="") = println(io, s)

    w("# Codebook — $(get(dp, "title", dp["name"]))\n")
    w("> **Generated file.** Do not edit by hand. Produced by " *
      "`scripts/build_codebook.jl` from `datapackage.json`. " *
      "Edit the schema and regenerate.\n")
    w("- **Dataset**: `$(dp["name"])`  ")
    w("- **Version**: $(get(dp, "version", "—"))  ")
    w("- **License**: $lic  ")
    w("- **Contributors**: $contribs  ")
    w("- **Rows**: $n_rows  ")
    w("- **Generated**: deterministically from `datapackage.json` (timestamps via Git history)\n")
    w("\n$(get(dp, "description", ""))\n")
    w("\n## Provenance\n")
    w("Attribution and timestamps are supplied by Git (`git blame` for line-level " *
      "history); releases are frozen and citable via a Zenodo DOI. Per-observation " *
      "coder attribution is carried in the `coder` field.\n")
    w("\n## Missing-value conventions\n")
    w("Absence is coded, never blank. These tokens are treated as missing by the " *
      "schema (`missingValues`):\n")
    w("\n| Token | Meaning |")
    w("|---|---|")
    w("| `.NR` | not recorded in the source |")
    w("| `.IL` | present but illegible / damaged |")
    w("| `.NA` | not applicable to this record type |")
    w("\n> `.ZERO` is **not** here: a source-recorded zero is the value `0`, a datum, " *
      "not an absence (see the `missingness` field).\n")
    w("\n## Variables at a glance\n")
    w("| # | Field | Type | Required | Coded values | Present |")
    w("|---:|---|---|:---:|---|---:|")
    for (i, f) in enumerate(fields)
        c = get(f, "constraints", Dict())
        req = get(c, "required", false) ? "✓" : ""
        enum = haskey(c, "enum") ? join(["`$v`" for v in c["enum"]], ", ") : ""
        cov = n_rows > 0 ? "$(present[f["name"]])/$n_rows" : "—"
        w("| $i | `$(f["name"])` | $(get(f, "type", "")) | $req | $(md_escape(enum)) | $cov |")
    end
    w("\n## Variable definitions\n")
    for f in fields
        c = get(f, "constraints", Dict())
        w("\n### `$(f["name"])` — $(md_escape(get(f, "title", "")))\n")
        w(md_escape(get(f, "description", "")) * "\n")
        bits = ["**type** $(get(f, "type", ""))"]
        get(c, "required", false) && push!(bits, "**required**")
        get(c, "unique", false) && push!(bits, "**unique**")
        haskey(c, "pattern") && push!(bits, "**pattern** `$(c["pattern"])`")
        haskey(c, "enum") && push!(bits, "**values** " * join(["`$v`" for v in c["enum"]], ", "))
        w("- " * join(bits, " · ") * "\n")
    end

    dest = joinpath(dataset_dir, "codebook.md")
    write(dest, String(take!(io)))
    return dest
end

function main()
    targets = if length(ARGS) >= 1
        [ARGS[1]]
    else
        sort([joinpath(DATASETS, d) for d in readdir(DATASETS)
              if isfile(joinpath(DATASETS, d, "datapackage.json"))])
    end
    for d in targets
        dest = build(d)
        println("wrote ", relpath(dest, ROOT))
    end
end

main()
