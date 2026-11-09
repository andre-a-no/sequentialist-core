# Sequentialist development roadmap

Audit date: **2026-11-09**. Status: **proposed implementation backlog**.
This document records work still to do; publishing it does not implement its
features, merge development branches or approve releases.

[Russian companion](ROADMAP.ru.md) · [Architecture and acceptance scenarios](docs/ecosystem-spec.md) · [Package catalog](docs/ecosystem-catalog.md)

The next milestone is a reproducibly installable, tested ecosystem with reliable
recovery and explicit limits on its conclusions. The largest immediate gaps are
branch/release integration, delivery of external notifications, resumable search
and interaction state, and application use of capabilities already in analysis.
Adding more algorithms alone will not close these gaps.

## 1. Scope and evidence

The audit compared the twelve repositories below, their default and selected
development branches, manifests, implementation, examples, existing backlogs and
GitHub Actions. Exact source revisions are recorded in section 8. This updates
the implementation priorities of the technical specification; its T-01–T-12
acceptance scenarios remain applicable. Earlier test counts in that specification
describe earlier development checks, not a new full-suite run in this audit.

Local checks on the audited source snapshots, under Python 3.12:

- All **28 core unittest tests passed** after editable installation of analysis
  and core. An initial source-path-only invocation could not discover installed
  CLI entry points; that invocation is not evidence of a core source defect.
- The games shared-resource example completed both jobs; the original agentic
  example completed without finding sufficient evidence; the reasoning example
  completed forward/backward/bidirectional derivation, finite-source retrieval
  and HTML export. A valid “no answer” outcome is not a failed run.
- This was not a rerun of every package's tests, a theorem audit, a load test or
  verification of every registry release. Existing CI results are listed below.

### Current package state

“Development” below means the selected branch in section 8, not an installed
public release. Missing Actions runs do not mean missing local tests.

| Package | Implemented baseline | Main remaining work | Backlog |
|---|---|---|---|
| `sequential-analysis` | Extensive statistical procedures, run/checkpoint contracts, Python and TypeScript executors | Assumption-aware composition, application-driven additions, release/conformance coverage | A01, F02, N01, B01, Q01, M01, H01 |
| `sequential-search` | Main has experiment/edge contracts; development adds checkpoint envelopes and finite implication reasoning | General finite traversal, persisted frontier/obligations, whole-search accounting | S01, S02, R01 |
| `sequential-games` | Development has explicit-state virtual-time simulation, delayed/private observations and in-memory continuation; main is a landing README | Validated durable state, explicit model/strategy comparison | G01, G02 |
| `sequentialist-core` | Journal, checkpoints, audit, file/SQLite storage, CLI, report and sink interfaces | Command validation, sparse sequence intake, durable notifications, reusable simulation summaries | C01–C03, N01, I01 |
| `sequentialist-visuals` | Development has standalone HTML/SVG search and event views; main is a landing README | Stable exchange records, adapters, privacy projections and scale limits | F01, V01 |
| `sequentialist-agentic` | Tool-agent baseline; development adds finite retrieval and trusted-rule reasoning examples | Package identity, measured task quality, evidence calibration and tool-effect contracts | F01, D01, I01 |
| `sequentialist-ab` | Experiment assignment, sequential analysis, guardrails and reports; TS assignment client | Integrate existing e-process support, reconcile decision/interval reporting, bound state cost | B01 |
| `sequentialist-quality` | Sequential lot inspection and sampling schemes | Finite-lot reference calculations, stopping/disposition metrics, variables scope | Q01 |
| `sequentialist-monitor` | Advisory monitoring, residual pipelines and alarm management | Reliable delivery, recovery-to-normal policy, calibration validation and first diagnosis pilot | M01 |
| `sequentialist-clinical` | Interim trial monitoring and committee reports | Tie handling, post-stop estimation and adaptation scope, report access integration | H01 |
| `sequentialist-search` | Reserved scope/documentation only | Decide whether a separate engineering wrapper is justified | X02 |
| `sequentialist-markets` | Reserved scope/documentation only | Specify and validate one historical monitoring use case | X01 |

Recent inspected test workflows succeeded for [analysis](https://github.com/andre-a-no/sequential-analysis/actions/runs/42535230775),
[core](https://github.com/andre-a-no/sequentialist-core/actions/runs/42535738111),
[ab](https://github.com/andre-a-no/sequentialist-ab/actions/runs/42535826776),
[quality](https://github.com/andre-a-no/sequentialist-quality/actions/runs/42535683099),
[monitor](https://github.com/andre-a-no/sequentialist-monitor/actions/runs/42535691942)
and [clinical](https://github.com/andre-a-no/sequentialist-clinical/actions/runs/42535747346).
The Actions API returned no runs for search, games, visuals or agentic, and their
inspected development trees had no workflows. The two reserved repositories also
had no runs. Green package CI does not establish cross-package compatibility.

### Existing capabilities that must not be rebuilt

- Public `canonical_json`/`loads` already exist; core imports them publicly.
- `Lagged` already forwards its inner guarantee. `Chain` still needs justified
  composition rules; taking the “weakest” label is not a sufficient argument.
- `BoundedABTest` already uses betting confidence sequences and advertises
  `log_e_value`; `RateRatioTest` also exposes an e-process. The A/B application's
  e-BH routing remains restricted to conversions. This is an integration backlog,
  not a request to invent those upstream capabilities.
- The TypeScript executor already exists, as do several regression/forecasting
  facilities. Audit coverage, installation and application adapters before adding
  another executor or generic “regression support” task.

These findings supersede the corresponding stale backlog descriptions, not the
permanent contribution/compatibility rules. Source anchors: [canonical][canonical],
[pipeline][pipeline], [A/B procedures][ab-methods], [rate procedures][rates],
[A/B routing][ab-routing], [TypeScript manifest][ts-manifest].

## 2. Ordering and completion gates

Priorities express dependencies and value, not calendar promises. Package names
identify responsibility; individual owners and effort estimates remain unassigned.
Independent work can proceed once its listed dependencies are satisfied.

| Gate | Priority | Deliverable | Exit evidence |
|---|---|---|---|
| G0: reproducible baseline | P0 | Selected implementations become an installable, CI-tested compatible set | F01/F02; tested branch decisions and package identities; fresh-environment examples |
| G1: dependable foundation | P0 | Accepted input, rejected commands, audit and notification delivery have separate explicit contracts | C01–C03 and A01; fault/replay cases and assumption declarations |
| G2: first integrated result | P1 | A bounded industrial diagnosis example and a finite reasoning/retrieval example, with resumable state and inspectable provenance | Relevant S/G/I/V/D/M tasks; T-01–T-11 evidence for the features each example uses |
| G3: application depth | P2 | Better A/B, lot-quality and trial workflows; defensible strategy comparisons | B01, Q01, H01, G02; independent numerical references and measured outcomes |
| G4: justified expansion | P3 | Selected market pilot, optional wrapper and scale work | A named consumer and acceptance workload for each X task |

G2 does not require every application to depend on games, agentic or visuals.
Use the smallest supported composition. A statistical guarantee, checked
derivation, interaction property and durable-delivery contract remain different
claims with different evidence.

## 3. P0 — integration and reliability

### F01 — integrate branches and establish package CI

**Owners:** search, games, visuals, agentic; coordination in core.

Compare development with the default branches, reconcile README/spec changes,
and prepare consolidation of the already implemented subsets. Resolve the
agentic manifest's distribution name `sequential-search` versus its repository
and import `sequentialist_agentic`; audit existing consumers before choosing a
rename/migration. Keep `sequential-search-core` distinct. Audit the old pinned
search commit against the features each example actually needs. Normalize the
clinical default-branch arrangement only as a separate, reviewed migration.

**Done when:** each implemented package has an automatic test/example workflow;
fresh installs import the intended distributions and expose their documented
CLI; chosen default branches contain the tested capabilities; old entry points
have a documented transition where needed. Branch merges remain separate owner
decisions. Evidence: [agentic manifest][agentic-manifest], section 8 trees.

### F02 — version and compatibility contract

**Owners:** all implemented packages. **Depends on:** F01 for new packages.

Record repository/distribution/import identities and a tested dependency matrix.
Retain Python 3.8 support for the established analysis/core applications; test
the Python 3.11+ intersections used by search/games/agentic/visuals. Check clean
wheel installation, packaged data, CLI discovery, npm/browser exports and actual
registry/tag/source version agreement. Pin unreleased dependencies explicitly.

**Done when:** every supported combination passes installation and a meaningful
cross-package example; supported checkpoint versions round-trip, unsupported
versions fail explicitly, and migrations have fixtures. Extend Python/TS
conformance for changed procedures, with declared numerical tolerances. A source
commit is not labelled a published release until publication is verified.

### C01 — validate commands and define invalid-input behavior

**Progress (unreleased):** the command preflight portion is implemented by
`Handler.check_command`; see [the contract](README.md#validate-commands-before-accepting-them)
and `CommandValidationTest` in [the recovery tests](tests/test_engine.py).
Application handlers must opt in. The broader invalid-observation policy work
below remains open; C01 as a whole is not complete.

**Owner:** core; domain validators stay in handlers.

At the audit baseline, domain argument validation happened in `on_command`,
after journaling. The new optional, side-effect-free check lets handlers refuse
invalid commands before acceptance. Remaining work: adopt domain checks in the
applications and make each stream's invalid-observation policy explicit and
persisted; distinguish rejection, recorded skip and task failure.

**Done when:** invalid domain arguments leave a usable task and do not enter its
accepted-command replay; accepted commands replay identically; rejected-input
diagnostics survive under their declared policy; old handlers still work and
checkpoint policy mismatches are detected. [Engine evidence][engine].

### C02 — sparse monotone sequence intake

**Owner:** core. Use analysis `Delivery.skip_range` through an explicit optional
intake policy rather than renumbering source records. Specify what a skipped
range means and how late records, duplicates and restarts behave. Retain the
current dense-sequence mode.

**Done when:** a long sequence with large gaps has bounded bookkeeping relative
to the declared retained state; duplicate/restart cases preserve state and audit;
late arrival into a skipped range is handled explicitly. [Engine evidence][engine].

### C03 — durable notification outbox

**Owner:** core, exercised by monitor and another command/report consumer.

The current engine checkpoints before notifying sinks; the webhook queue is
in-memory and abandons an entry after its retry limit. Add persistent pending
delivery records, stable delivery identities, acknowledgement, bounded retries,
dead-letter inspection and backpressure. Couple audit/checkpoint/outbox recovery
for each durable storage backend.

**Done when:** injected crashes before/after checkpoint, send and acknowledgement
lose no committed pending delivery; retries preserve the identity; slow receivers
cannot cause unbounded RAM growth. Promise **at-least-once delivery** under stated
storage/retry assumptions and require idempotent receivers for effects. Do not
claim exactly-once external effects. [Engine][engine], [sinks][sinks].

### A01 — assumptions and composed guarantees

**Owner:** analysis; core/applications carry the resulting metadata unchanged.

Specify the assumptions connecting transforms, estimators and tests. A pipeline
with an estimated model cannot acquire exact validity just because its final
test has an `exact` label. Keep unsupported compositions at `none` or another
explicitly justified status; labels are not a universal ordered lattice.

**Done when:** supported compositions have a reference/derivation and tests;
incompatible inputs or assumptions produce a visible refusal/downgrade; reports
separate assumptions from calibration diagnostics. Cover `Chain`, fitted
residuals and adaptive allocation. [Pipeline evidence][pipeline].

## 4. P1 — resumable methods and the first integrated examples

| ID / owner | Work and dependencies | Acceptance evidence |
|---|---|---|
| **N01 / analysis + core** | Add reusable run-length/cost summaries: stopping probability, censoring fraction, expected/restricted run length and justified Monte Carlo intervals. Mathematical estimators belong in analysis, pipeline aggregation in core. | Known finite/geometric examples and heavy-tail/censored cases; no silent treatment of a simulation cap as a completed stopping time. Reproducible seeds and JSON reports. |
| **S01 / search** | Complete a finite reference traversal with canonical state/context identity, AND obligations, cycle handling, explicit stop reasons and separate search cost/proof cost. Build on existing finite reasoning rather than replacing it. Depends on F01/A01 where statistical evidence is used. | Exhaustive small-graph reference comparisons; missing premises, incompatible contexts, unreachable goals and budget exhaustion remain distinguishable. T-01–T-04, T-11. |
| **S02 / search** | Persist the actual frontier, obligations, selected policy state, RNG and accounting, including suspend/withdraw/resume semantics. Existing graph/Run serialization is only part of this. Depends on S01. Begin with conservative, non-recycled error budgets where a validated allocation applies. | Interrupt after every small-example step; restored and uninterrupted decisions/proofs/costs match. No double charging or double evidence after reopening. Reject incompatible model/codecs. T-09/T-11. |
| **G01 / games** | Add a validated, versioned state codec with model/policy identity, pending events/actions, local observations and independent RNG states. Depends on F01; retain current virtual-time semantics. | Serialized resume matches uninterrupted traces including actions in flight; hidden/private information remains hidden after restore. Invalid states/versions rejected. Equal-time ordering documented without a simultaneous-move claim. T-06–T-09. |
| **I01 / core + consuming applications** | Specify adapters for durable search/game tasks and external tool receipts. Keep algorithm state owned by methods and I/O effects owned by engineering/application code. Depends on C01–C03 and relevant S02/G01. | Crash/retry/duplicate/delay scenarios preserve action identity and budget accounting; an intention, admission and completion are separate events. T-07/T-09–T-11. Follow core's existing admission rule for new generic APIs; prove reuse in at least four application packages before promoting a new general facility into core. |
| **V01 / visuals + adapters** | Version minimal input records for graphs, findings and event views; derive them through read-only adapters. Depends on the relevant method contracts, not a new universal schema framework. | Escaping and input immutability checks; recipient-safe projection before rendering; graph/timeline links preserve provenance; large-input limits/aggregation measured. Offline export works without hidden network requests. |
| **D01 / agentic** | Stabilize finite retrieval and rule-based reasoning, outcome taxonomy and source lineage. Separate heuristic evaluator scores from calibrated statistical evidence; add real tools only after receipt/timeout semantics. Depends on F01, S01/S02, and I01 for live effects. | Fixed benchmark with grounded reference answers/rules, missing-answer cases, duplicated sources, timeouts and conflicting evidence; report validity and acquisition cost. Any FWER/FDR claim requires a valid evidence construction and whole-search allocation. |
| **M01 / monitor + analysis** | First integrated domain pilot: recommend the next diagnostic measurement among a finite set of equipment causes, independently of LLMs. In parallel, validate fitted residuals and a recovery-to-normal policy beyond “no alarm for N windows.” Depends on C01–C03, A01/N01 and S01 for diagnosis. | Stable/step/drift/missing/duplicate/restart scenarios; false alarms per exposure, detection-delay distribution and alarm-clear oscillations reported. Hold out calibration data; check small persistent shifts. T-05 plus relevant delivery/replay cases. CUSUM ARL calibration must name a model and numerical reference, not rely on the class's guarantee label. |

Sources: [simulation summaries][simulate], [search checkpoint][search-checkpoint],
[search reasoning][search-reasoning], [games simulation][games-simulation],
[visual renderer][visual-render], [agentic evidence][agentic-evidence],
[monitor limitations][monitor-readme].

## 5. P2 — deepen applications and compare strategies

| ID / owner | Scope and dependencies | Done when |
|---|---|---|
| **B01 / ab + analysis** | Integrate existing bounded/rate e-processes into eligible multiplicity families; label FDR decisions and confidence coverage separately. Benchmark interval behavior for rare outcomes; add a specialised interval only if the current betting method leaves a measured gap. Depends on A01/F02; N01 for pipeline studies. | Mixed-metric tests and null simulations support the chosen correction under stated assumptions; reports explain why a rejection and interval need not coincide. Adaptive allocation uses recorded assignment propensities. Unit-state/checkpoint growth is measured before changing storage. |
| **Q01 / quality + analysis** | Add finite-lot sampling without replacement, reference OC/ASN and decision-conditioned stopping summaries; derive AOQ/AOQL/ATI only for a specified rectification policy. Expand variable sampling beyond the supported known-sigma/one-sided subset separately. Depends on N01 and validated upstream methods. | Tiny finite lots agree with exhaustive enumeration, large-lot limits agree with the supported approximation, truncated plans report their residual decision rule. No automatic claim of conformity to an external sampling standard. |
| **H01 / clinical + analysis** | Prioritise tied-event handling and stopping-adjusted effect reporting; then conditional power/re-estimation only with a stated design. Retain explicit small-sample/estimated-sigma limitations. Safety methods such as MaxSPRT or risk-adjusted CUSUM require separate upstream work. Depends on A01/F02/N01. | Tied and untied datasets match a named independent reference; stopped trials are checked by simulation under the chosen design. Open/closed reports are delivered through access controls of the hosting application, not merely separated files. This milestone concerns trial monitoring; diagnosis/treatment planning requires a separate scope and validation. |
| **G02 / games + domain adapters** | Define one bounded model with explicit participant objectives, allowed information, utilities/costs and admissible actions; compare policies against a simple baseline. Add simultaneous moves or cancellation only when that model requires them. Depends on G01/N01. | Same scenario/noise seeds, declared information sets and all objective components reported; liveness/fairness/regret claims only for model classes with evidence. T-12. |
| **R01 / search + analysis** | Research adaptive alpha allocation, reopening/refund rules and heuristic/value-of-information search after conservative traversal works. Depends on S02/A01/N01. | Whole-search validity argument under stated adaptivity/dependence assumptions, adversarial small cases and comparison with the conservative baseline. Simulation alone does not certify an exact error bound. Retain the conservative policy if the proof is unavailable. |

Applications can take additive improvements earlier when their dependencies are
met. New statistical formulas belong in analysis; applications define the domain
question, validation data and presentation. Delivery, persistence and UI changes
must not silently change the inferential target.

## 6. P3 — expansion only with a concrete consumer

- **X01 / markets:** start with one observational historical strategy-decay or
  risk-monitoring pilot. Specify event/availability time, leakage-free inputs,
  baselines and costs/slippage where relevant. Gate: held-out chronological
  replay with declared monitoring metrics and restart behavior. Trading execution
  and profitability claims are outside this first milestone.
- **X02 / sequentialist-search:** keep the reserved repository until at least two
  actual consumers demonstrate duplicated search-job engineering. Decide whether
  an adapter in existing packages or a separate wrapper is smaller. If a wrapper
  is justified, it must reuse persistence/audit mechanisms rather than create a
  competing runtime. This two-consumer discovery gate does not replace core's
  stricter rule for adding generic APIs.
- **X03 / storage and runtime:** benchmark state size, checkpoint/replay latency,
  peak memory and receiver backlog using declared representative workloads.
  Introduce incremental storage, distributed ownership or Postgres only where
  those measurements show a need. Acceptance includes fencing/lease-loss faults
  before making multi-host single-writer claims. The current single-host design
  remains a supported deployment option.

`release`, `mlops`, `messengers` and `connectors` remain proposed scopes. Do not
create packages merely to fill the ecosystem diagram. Broad GUIs, unrestricted
agents and distributed executors are not prerequisites for the first useful
integrated release.

## 7. First implementation queue and definition of done

Recommended first queue, with independent items allowed to overlap:

1. **F01/F02:** CI, distribution identity and one reproducible dependency set.
2. **C01:** pre-journal command validation and explicit invalid-input behavior.
3. **C02:** sparse sequence intake and restart regression cases.
4. **C03:** durable outbox and crash/receiver-failure cases.
5. **A01/N01:** assumption-aware reporting and reusable evaluation summaries.
6. **S01/S02:** finite traversal plus actual continuation, with conservative budgets.
7. **G01:** durable interaction state with observation isolation.
8. **I01/V01/D01/M01:** adapters, provenance views and the two bounded examples.

For every item, completion requires: a public contract and limitations; the
implementation in its owning package; meaningful reference/fault/regression
checks; a working installed example; compatibility/migration evidence for changed
state; and updated user documentation. Record the implementation revision and
test run beside the item before changing its status. A draft document, a class
name or a successful demo alone does not close a statistical or reliability claim.

## 8. Audited source revisions

The snapshot predates this roadmap commit. Default-branch history and selected
development code are deliberately distinguished. Links below pin the evidence
even if branches move.

| Repository | Default branch / revision | Inspected branch / revision |
|---|---|---|
| [sequential-analysis](https://github.com/andre-a-no/sequential-analysis) | `main` / [b156ef52](https://github.com/andre-a-no/sequential-analysis/tree/b156ef520ca5c56beaf9b7e453fa43b9bba94574) | `main` / [b156ef52](https://github.com/andre-a-no/sequential-analysis/tree/b156ef520ca5c56beaf9b7e453fa43b9bba94574) |
| [sequential-search](https://github.com/andre-a-no/sequential-search) | `main` / [24884559](https://github.com/andre-a-no/sequential-search/tree/248845598053aa8b9efcc4e5845273c55d846756) | `feat/checkpoint-reasoning-and-discovery` / [44201753](https://github.com/andre-a-no/sequential-search/tree/442017531c448dcd07556e78b11630dc7020e1b6) |
| [sequential-games](https://github.com/andre-a-no/sequential-games) | `main` / [57eaf24a](https://github.com/andre-a-no/sequential-games/tree/57eaf24aab13ecc35f57e60b12c9dbaa59966da2) | `feat/explicit-state-games-and-discovery` / [64ad15dd](https://github.com/andre-a-no/sequential-games/tree/64ad15ddd3cd79a922384715b5ad8f781287cca5) |
| [sequentialist-core](https://github.com/andre-a-no/sequentialist-core) | `main` / [e4ff5aad](https://github.com/andre-a-no/sequentialist-core/tree/e4ff5aad5f9a3ed0ce0f6e42cb858e4ec42bd18e) | `main` / [e4ff5aad](https://github.com/andre-a-no/sequentialist-core/tree/e4ff5aad5f9a3ed0ce0f6e42cb858e4ec42bd18e) |
| [sequentialist-visuals](https://github.com/andre-a-no/sequentialist-visuals) | `main` / [3af5c3b1](https://github.com/andre-a-no/sequentialist-visuals/tree/3af5c3b18c6d5aae2e3630a88bb17a607d82ef52) | `feat/portable-views-and-discovery` / [8643f7e2](https://github.com/andre-a-no/sequentialist-visuals/tree/8643f7e247799428802e867b205833bdecd3d202) |
| [sequentialist-agentic](https://github.com/andre-a-no/sequentialist-agentic) | `main` / [99372150](https://github.com/andre-a-no/sequentialist-agentic/tree/993721502d84dba736ded86888a2cf554ac2f06b) | `feat/reasoning-tasks-and-discovery` / [daab16d4](https://github.com/andre-a-no/sequentialist-agentic/tree/daab16d413dbf0f4aa49836751a444fd71813295) |
| [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) | `main` / [ad639d5d](https://github.com/andre-a-no/sequentialist-ab/tree/ad639d5d575db83e7c4320bcd856e9f17cd5c936) | `main` / [ad639d5d](https://github.com/andre-a-no/sequentialist-ab/tree/ad639d5d575db83e7c4320bcd856e9f17cd5c936) |
| [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality) | `main` / [b599e298](https://github.com/andre-a-no/sequentialist-quality/tree/b599e298e2c5dca454ea0e5922526a88cc810bab) | `main` / [b599e298](https://github.com/andre-a-no/sequentialist-quality/tree/b599e298e2c5dca454ea0e5922526a88cc810bab) |
| [sequentialist-monitor](https://github.com/andre-a-no/sequentialist-monitor) | `main` / [253d7404](https://github.com/andre-a-no/sequentialist-monitor/tree/253d7404e848672c6099a9cd7a876c5229eb59c0) | `main` / [253d7404](https://github.com/andre-a-no/sequentialist-monitor/tree/253d7404e848672c6099a9cd7a876c5229eb59c0) |
| [sequentialist-clinical](https://github.com/andre-a-no/sequentialist-clinical) | `claude/gracious-davinci-jgkev7` / [f80b6239](https://github.com/andre-a-no/sequentialist-clinical/tree/f80b6239690d19823255d3ed70a62a13c622eaa6) | `claude/gracious-davinci-jgkev7` / [f80b6239](https://github.com/andre-a-no/sequentialist-clinical/tree/f80b6239690d19823255d3ed70a62a13c622eaa6) |
| [sequentialist-search](https://github.com/andre-a-no/sequentialist-search) | `main` / [9c126e2a](https://github.com/andre-a-no/sequentialist-search/tree/9c126e2a377c4f99e6daf6bc166a6346cd0a0a3a) | `docs/planned-scope-and-discovery` / [30c91636](https://github.com/andre-a-no/sequentialist-search/tree/30c9163629a9eff9df5bded8a6ac716b1687d9e1) |
| [sequentialist-markets](https://github.com/andre-a-no/sequentialist-markets) | `main` / [afb359d8](https://github.com/andre-a-no/sequentialist-markets/tree/afb359d8e1d9bb2e4b10c69eeea4bde28d6b7ce1) | `docs/planned-scope-and-discovery` / [7ab9b665](https://github.com/andre-a-no/sequentialist-markets/tree/7ab9b665071d9ae0d13253f810e2b58e7e2f227f) |

[canonical]: https://github.com/andre-a-no/sequential-analysis/blob/b156ef520ca5c56beaf9b7e453fa43b9bba94574/src/sequential_analysis/canonical.py
[pipeline]: https://github.com/andre-a-no/sequential-analysis/blob/b156ef520ca5c56beaf9b7e453fa43b9bba94574/src/sequential_analysis/pipeline.py
[ab-methods]: https://github.com/andre-a-no/sequential-analysis/blob/b156ef520ca5c56beaf9b7e453fa43b9bba94574/src/sequential_analysis/procedures/ab.py
[rates]: https://github.com/andre-a-no/sequential-analysis/blob/b156ef520ca5c56beaf9b7e453fa43b9bba94574/src/sequential_analysis/procedures/rates.py
[ab-routing]: https://github.com/andre-a-no/sequentialist-ab/blob/ad639d5d575db83e7c4320bcd856e9f17cd5c936/src/sequentialist/ab/analysis.py
[ts-manifest]: https://github.com/andre-a-no/sequential-analysis/blob/b156ef520ca5c56beaf9b7e453fa43b9bba94574/ts/package.json
[agentic-manifest]: https://github.com/andre-a-no/sequentialist-agentic/blob/daab16d413dbf0f4aa49836751a444fd71813295/pyproject.toml
[engine]: https://github.com/andre-a-no/sequentialist-core/blob/e4ff5aad5f9a3ed0ce0f6e42cb858e4ec42bd18e/src/sequentialist/core/engine.py
[sinks]: https://github.com/andre-a-no/sequentialist-core/blob/e4ff5aad5f9a3ed0ce0f6e42cb858e4ec42bd18e/src/sequentialist/core/sinks.py
[simulate]: https://github.com/andre-a-no/sequentialist-core/blob/e4ff5aad5f9a3ed0ce0f6e42cb858e4ec42bd18e/src/sequentialist/core/simulate.py
[search-checkpoint]: https://github.com/andre-a-no/sequential-search/blob/442017531c448dcd07556e78b11630dc7020e1b6/src/sequential_search/io/checkpoint.py
[search-reasoning]: https://github.com/andre-a-no/sequential-search/blob/442017531c448dcd07556e78b11630dc7020e1b6/src/sequential_search/reasoning.py
[games-simulation]: https://github.com/andre-a-no/sequential-games/blob/64ad15ddd3cd79a922384715b5ad8f781287cca5/src/sequential_games/simulation.py
[visual-render]: https://github.com/andre-a-no/sequentialist-visuals/blob/8643f7e247799428802e867b205833bdecd3d202/src/sequentialist/visuals/render.py
[agentic-evidence]: https://github.com/andre-a-no/sequentialist-agentic/blob/daab16d413dbf0f4aa49836751a444fd71813295/src/sequentialist_agentic/evidence.py
[monitor-readme]: https://github.com/andre-a-no/sequentialist-monitor/blob/253d7404e848672c6099a9cd7a876c5229eb59c0/README.md
