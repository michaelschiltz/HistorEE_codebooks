# `RD-test`: the characteristic under test

`RD-test` is a placeholder name for a characteristic that is **not** in the vocabulary. You are coding it, and five existing characteristics beside it, on nineteen rulebooks. Code it exactly as defined here. If the definition does not fit a rule you read, say so in a note and in answer 4, and do not bend the definition to make it fit.

## Definition

*Once a member has drawn from the fund and stops repaying, and his own security is exhausted or fails, who does the instrument make liable for what remains unpaid?* His own security means his guarantors, co-signers and collateral.

- **Facet** loss sharing. **Value type** nominal. **Locator** `arrangement`.
- **Component** `loss-sharing`, **work package** WP1.
- **Applicability.** `.NA` where no payout creates a debt owed to the fund.

## Values

| value               | meaning                                                                         |
|---------------------|---------------------------------------------------------------------------------|
| `fund`              | the loss is absorbed by the fund or its reserve                                 |
| `all-members`       | the members are jointly liable for it                                           |
| `standing-subgroup` | a group the rules set up in advance, liable because the defaulter belongs to it |
| `officers`          | the officers are liable for the default itself                                  |
| `deferred`          | the instrument refers the default itself to the members' decision               |

`.NR` and `.NA` as in `CONTRIBUTING.md`. There is no `0` and no `P`.

## Coding rules

1. **The line with `RB3`.** Guarantors or co-signers chosen for a particular loan are security and belong in `RB3`, even when they must come from the defaulter's group. A group that answers by membership is `standing-subgroup`. The test is whether liability attaches by signing or by belonging.
2. **Code the last bearer the instrument names.**
3. **Officers' liability for mishandling only** (handling contrary to the rules, negligence) is not `officers`. Code `.NR` and say so in the note.
4. **The defaulter's own liability is not this characteristic.** That includes his liability for the shortfall when a pot is re-auctioned because he refused it or failed to complete.
5. **An unwon member's default is not this characteristic.** A member who stops contributing before he has drawn is `CN3`'s ground; record what happens to him in `CN3`'s note.
6. **Silence is `.NR`.** Never code what the law or custom would have supplied when the rules say nothing. A clause that sends unprovided matters to local custom is `.NR`; say so in the note.
7. **`deferred` needs a clause about default itself.** A general amendment clause, or one putting 'necessary matters' to the members, is not `deferred`. Only a clause that refers a member's default to the members' decision can be.

## The relation to `LS1`

`LS1` asks *how* an unmet loss is divided (`pro-rata`, `equal`, `capped`); `RD-test` asks *who* bears it. `LS1` also carries the value `residual-on-fund`, which says the same thing as `RD-test`'s `fund`. That overlap is known and is not yours to repair. Where a rule puts the loss on the fund, code `LS1 = residual-on-fund` **and** `RD-test = fund`, and say in both notes that the two cells rest on one clause.

## Which rulebooks are in scope

**The population is defined by structure, not by name.** A rulebook is in scope if it sets up a fund to which members contribute in rounds and from which a member receives a pot (in money or in kind) that he must then repay or keep contributing towards, whatever the fund is called: 頼母子講, 無盡講, 模合, 和合講 or anything else. A rulebook listed in `FRAMES.md` that turns out to set up no such payout (a savings club that only accumulates and returns) is still coded: `RD-test`, `RB3` and any other cell whose ground is absent are `.NA`, argued in the note. 十錢講 and 信用會 rules printed beside the listed rulebooks are **out of scope**; do not read them.
