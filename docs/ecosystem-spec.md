# Sequentialist ecosystem: unified technical specification

Version: 0.3 draft · 2026-11-02

This document describes the target architecture and acceptance requirements.
It is not a claim that all capabilities already exist. Existing public APIs
remain supported; any incompatible change requires an explicit migration plan.

## 1. Purpose

Build a family of composable libraries for reaching goals from available
knowledge through observation, inference, experimentation and action, while
accounting for uncertainty, resources, time and the actions of other participants.

A task may ask the system to discover an answer, derive a proof, diagnose a
cause, choose an intervention, monitor a process, or coordinate with another
participant. It must be possible to explain what was known, what was assumed,
why an action was selected, what actually happened, and why execution stopped.

## 2. Architectural principles

- **A-01 — Separate decisions from execution.** Statistical procedures infer;
  search strategies select expansions; participant policies propose intentions;
  runtimes execute and deliver events. Decision logic performs no hidden I/O.
- **A-02 — Preserve methodological and engineering boundaries.** sequential-*
  primarily contains mathematics, cybernetics, pure algorithms and abstractions
  of those algorithms. sequentialist-* contains software engineering and
  application software. General applicability alone does not put an execution
  framework, storage system or integration adapter in sequential-*.
- **A-03 — Knowledge is local.** World state, participant knowledge, hypotheses,
  assumptions and verified conclusions are distinct objects.
- **A-04 — Time matters.** The environment may change during deliberation,
  transmission, execution and deliberate inactivity.
- **A-05 — Guarantees are explicit.** Every claim names its meaning, scope,
  assumptions, method and supporting evidence. Composition never silently
  strengthens a guarantee.
- **A-06 — Persistence is semantic.** Restoring a task preserves its knowledge,
  obligations, evidence, reservations and outstanding work, rather than merely
  reconstructing an object graph.
- **A-07 — Reuse is optional.** Applications can use search without LLMs, games
  without search, and statistics without application storage.
- **A-08 — Demonstrate generality.** Shared abstractions must support distinct
  executable examples before they become mandatory across applications.

## 3. Package responsibilities and dependencies

### 3.1 Three logical layers, two naming families

| Layer | Naming | Responsibility |
|---|---|---|
| Mathematical and cybernetic methods | sequential-* | Formal models, algorithmic abstractions, algorithms, assumptions, correctness conditions and reference computations |
| Reusable software engineering | sequentialist-core, sequentialist-visuals and other engineering packages/modules | Runtimes, services, delivery, storage, recovery, application schemas, audit, reusable visualization and operational adapters |
| Application software | sequentialist-agentic and domain/UI packages | Concrete tasks, models, integrations, workflows and user-facing behavior |

These are three architectural layers; a third naming prefix is not required.
sequentialist-* deliberately spans both engineering and application layers.
The engineering platform is an open family of packages, not another name for
sequentialist-core. Core owns common application execution infrastructure;
visuals owns reusable visualization and inspection. Future engineering packages
can own distinct demonstrated responsibilities without becoming domain
applications or being absorbed into core. Do not invent those packages in
advance of a concrete need. Some adapters can remain in their application
package until they satisfy the existing criterion for sharing code in core.

The methodological API describes transitions from explicit state, observations,
actions and random inputs to updated state and outputs. It does not secretly
read a clock, perform I/O or schedule physical work. Internal implementation
optimizations need not require every object to be immutable. Application
parameters and subject-specific models can also be pure; purity alone does not
make subject-specific code a reusable mathematical library.

For example, asynchronous timing, partial observability, admissibility and
joint-action resolution are mathematical model semantics. Running workers,
choosing asyncio or a broker, delivering messages, dispatching tools, retrying
requests and operating a service are engineering responsibilities. A scheduler's
algorithm may have a mathematical abstraction; its operational implementation
and external integrations belong to sequentialist-*.

A reference simulator may belong to sequential-games when it is an explicit,
reproducible computation over a model, algorithm state and random inputs. It is
not the production interaction runtime. Likewise, an algorithmic state envelope
may belong to sequential-search, while durable capture, storage, migration
execution and restart orchestration belong to the engineering layer.

### 3.2 Packages

| Package | Owns | Does not own |
|---|---|---|
| sequential-analysis | Statistical procedures, inference state, calibration algorithms, declared statistical guarantees | Application objectives, tool execution, operational scheduling |
| sequential-search | Abstract search states/transitions, AND/OR obligations, search algorithms, algorithmic state envelopes and resource-accounting rules | Operational search jobs, domain inference rules, tool execution, LLM prompts |
| sequential-games | Formal participant/environment models, information structures, policy algorithms, interaction semantics and reference simulation | Production participant orchestration, communication infrastructure, live executors, a universal optimal strategy |
| sequentialist-core | Reusable engineering: declarative application specs, durable execution, journal, storage, audit, replay, reports and runtime adapters | New statistical/search/game methods or subject-specific decisions |
| sequentialist-agentic | LLM/tool adapters, agent policies, retrieval and reasoning examples, evaluator calibration interfaces | Mandatory execution layer for every domain package |
| sequentialist-visuals | Engineering-platform visualization: reusable search, interaction, uncertainty and audit views; inspection and export | Subject-specific decision rules, hidden changes to decision state or promotion of an unsupported claim |
| Domain packages | Subject states, actions, constraints, rule sets, validators, objectives and reporting | Copies of the common statistical/search/interaction engines |

### 3.3 Dependency and compatibility rules

1. sequential-analysis remains independently usable with its existing minimal
   runtime requirements. Its Python and TypeScript implementations share only
   the procedures explicitly supported by both.
2. The contract layers of sequential-search and sequential-games use the
   standard library. Statistical and planning integrations are optional adapters.
3. sequentialist-core remains independently usable for monitoring applications.
   A search or game task integrates through a Handler/adapter, not a second
   application journal with competing sources of truth.
4. Domain packages may depend directly on search or games. They do not have to
   depend on agentic. Integration modules must avoid circular imports between
   search, games, core and agentic.
5. Preserve current package identities and interpreter support. Existing
   analysis/core Python 3.8 support is not raised merely because new search,
   agentic and games packages require Python 3.11 or later.
6. Existing core responsibilities stay there. New features enter core when
   they satisfy the family's existing shared-use criterion; this document does
   not authorize moving existing APIs out of core.
7. Runtime code already exposed by sequential-* is an existing compatibility
   fact, not the target placement rule for new engineering features. Retain
   supported APIs; any future separation requires a dedicated inventory,
   compatibility adapter and migration decision rather than mass relocation.

## 4. Shared conceptual contracts

These are semantic requirements, not a requirement to put every type in one
new shared package. Each record has an owner and explicit integration mappings.

| Concept | Required meaning |
|---|---|
| Goal | Desired condition, result validator, constraints, version and termination criteria |
| Knowledge | Facts, source observations, derivations, assumptions and unresolved uncertainty, with provenance |
| Observation | Information actually delivered to a recipient, with source, identity and timing |
| Search state | Relevant knowledge, goals/subgoals, outstanding obligations and domain context |
| Transition | Operation with preconditions, effects or derived results, cost and provenance |
| Intention | Proposed action tied to the information used to choose it; not an execution receipt |
| Event | Occurrence with identity, time semantics, recipient scope and causal links |
| Constraint | A subject-defined admissibility condition; hard constraints are not traded away implicitly |
| Evidence | Method-specific support for a claim, including its assumptions and data lineage |
| Outcome | Validated result, remaining obligations, stop reason, costs and guarantees |

Costs are vectors where appropriate: compute, queries, money, elapsed time,
energy and subject-specific quantities. Statistical alpha, clinical harm,
financial exposure, utility and elapsed time are separate dimensions. Any
scalarization or exchange rule is a declared application decision.

## 5. Search requirements

### 5.1 State and expansion

- **S-01:** Support forward expansion: derive consequences or obtain observations
  from available state.
- **S-02:** Support backward expansion: identify sufficient premises for a goal.
  Every expansion records the justification that those premises imply the goal.
  A backward expansion need not be an inverse executable action.
- **S-03:** Support bidirectional search with a checked connection between
  forward results and backward requirements. Matching text or an embedding is
  not sufficient to establish a proof connection.
- **S-04:** Represent OR alternatives and AND obligations. A transition requiring
  several premises succeeds only when all required premises are satisfied.
- **S-05:** Backward search may produce conditional results: a conclusion with
  an explicit list of missing premises. Such a result is not an unconditional proof.
- **S-06:** Distinguish domain state from an experiment that acquires information
  about that state. Provide explicit adapters for the current Node experiment
  contract; do not silently redefine existing Node.step semantics.

### 5.2 Identity and search control

- **S-07:** Canonicalization includes the context needed for equivalence: relevant
  assumptions, goal version, environment/model version and temporal scope.
  An unchanged observation or equivalent derivation must not be counted twice.
  Re-measuring a changed environment can be a new experiment.
- **S-08:** Preserve different derivations when provenance or assumptions differ,
  even if their displayed conclusion is the same. Detect cyclic justification;
  a goal cannot justify itself. Represent repeated world states without
  requiring that the evolving world itself be acyclic.
- **S-09:** Separate the result validator from the expansion-selection strategy.
  Start with exhaustive and cost-ordered baselines. Add heuristic, bandit or
  information-value strategies behind the same interface.
- **S-10:** Make each strategy's completeness and optimality conditions explicit.
  A resource-limited or heuristic run must not claim that no solution exists
  merely because it found none.
- **S-11:** Allow suspension, explicit withdrawal and resumption without resetting
  knowledge, evidence or obligations. ACCEPT/REJECT concern a declared test;
  WITHDRAW concerns continuation. RESUME is a transition, not a data verdict.
- **S-12:** Report distinct stop reasons: validated goal, exhausted search under
  stated assumptions, resource limit, deadline, withdrawal, missing premises,
  invalid input and execution failure.
- **S-13:** Define an algorithmic state envelope preserving frontier order,
  transition identities, evidence, allocations, policy state and random state.
  Engineering adapters capture/store it through versioned checkpoints and
  coordinate it with outstanding external work.

Stopping a branch and selecting another one need not require statistics in
every application. If a statistical guard is used, its null/model and validity
conditions must be defined. An e-value is not a probability that a branch wins.

## 6. Interaction and sequential-games

The G requirements define mathematical/cybernetic semantics and algorithmic
behavior. They do not assign operational runtime implementation to games.

- **G-01:** Support one or more participants with separate objectives,
  observations, resources and policies. Objectives may coincide, conflict or
  overlap partially. Cooperative, competitive and general-sum cases are explicit.
- **G-02:** Environment dynamics depend on current world state, participant
  actions and declared stochastic inputs. The environment can also evolve
  without participant actions.
- **G-03:** Define sequential, simultaneous and asynchronous interaction through
  explicit model-time and action-order semantics. A virtual-time reference
  simulator is the first executable interpretation of the model. Equal-time
  event ordering is specified and included in its trace; a sequential tie-breaker
  is not advertised as simultaneous joint-action resolution. Live scheduling is
  implemented in the engineering layer.
- **G-04:** Policies receive only authorized observations and their own history.
  Observation values reflect their generation time, even if delivery is delayed.
  A policy is never passed the simulator's hidden world state or private RNG.
- **G-05:** Represent deliberate inactivity explicitly: no intervention, waiting
  for an event, waiting until a deadline and withdrawal. Unavailability due to
  failure or an unfinished action is a separate runtime condition.
- **G-06:** Waiting does not freeze clocks or other participants. Delay and
  foregone opportunities can affect utility, state and constraints.
- **G-07:** Actions can have duration and delayed effects. Deliberation, admission,
  execution and notification may occur at different times. Independent pending
  actions must not block one another.
- **G-08:** Define action admissibility at the model's declared admission/commit
  point. Record the observations on which the intention was based; a stale
  decision may be rejected or reconsidered. Engineering adapters implement the
  corresponding admission and execution protocol against real systems.
- **G-09:** Rules for competing actions on shared resources are explicit. Fairness,
  priority, reservation and commitment are policies/protocols, not accidental
  consequences of thread scheduling.
- **G-10:** Preserve participant departure semantics: already accepted actions
  and obligations require explicit completion or cancellation handling.

The library supplies interaction primitives and measured outcomes. Equilibrium,
regret bounds, reachability probabilities or optimal control require separate
algorithms and assumptions; none follows automatically from a statistical test.

## 7. Runtime, events and persistence

These are software-engineering requirements owned by sequentialist-*.
Application-specific implementations can precede shared core abstractions.
They interpret the mathematical contracts without duplicating their algorithms.

- **R-01:** Give actions and events stable identities, correlation/causal links,
  actor/source identity and versioned payload schemas. Distinguish source time,
  delivery time and processing time where they differ.
- **R-02:** Specify duplicate, missing and out-of-order event handling per stream.
  Preserve the core's existing idempotent intake; source ordering constraints
  must not be confused with a universal total order of distributed events.
- **R-03:** Track action lifecycle: proposed, submitted, admitted/rejected,
  running, completed/failed and cancellation requested/confirmed. Sending a
  cancellation request does not prove that a physical effect was prevented.
- **R-04:** Declare adapter support for retries, idempotency and recovery. Do not
  promise exactly-once physical effects without support from the destination.
- **R-05:** A runtime failure is not a domain rejection or a proof of futility.
  Recovery policy and participant policy can react differently.
- **R-06:** Persist unresolved intentions, accepted actions, scheduled events,
  subscriptions, timers, observations, participant state, RNG, model versions
  and budget reservations at a consistent boundary.
- **R-07:** A simulation restored under the same supported versions, scheduling
  rules and random states produces the same subsequent events and outcomes.
  Checkpoints use explicit trusted codecs, never executable imports from data.
- **R-08:** Replay external observations and action receipts from the journal.
  Reissuing an external action is a separate authorized execution mode, not a
  consequence of replay. A seed alone cannot reproduce an external service.
- **R-09:** Separate random streams where required for environment dynamics,
  participant policies and statistical procedures. Record their allocation so
  scheduling changes do not silently alter unrelated sources of randomness.

Initial reference simulations or engineering runtimes may implement a documented subset of this lifecycle.
Unsupported cancellation, durable execution or distributed semantics must be
visible in capability descriptions rather than inferred from the API name.

## 8. Evidence, correctness and assurance

- **E-01:** Preserve the existing statistical guarantee vocabulary: exact,
  asymptotic, model, approximate and none, with explicit assumptions and scope.
- **E-02:** Record formal/logical verification separately: validator identity,
  rule set, checked derivation and unresolved assumptions. A statistical exact
  guarantee is not a formal proof, and a proof does not calibrate an estimator.
- **E-03:** Mark heuristic relevance scores and uncalibrated LLM judgments as
  heuristic. Converting a score to a likelihood ratio does not establish an
  e-process without a valid conditional model or calibration argument.
- **E-04:** For whole-search error control, specify the claim family, adaptive
  selection assumptions, dependence handling and allocation rule. Local test
  validity is insufficient to establish global FWER/FDR.
- **E-05:** Alpha refund and re-reservation under repeated WITHDRAW/RESUME require
  their own justified accounting rule. Preservation of numerical totals alone
  is not a proof of validity.
- **E-06:** Simulation estimates include replication count, seeds, uncertainty
  intervals and model assumptions. Keep empirical findings separate from
  mathematical bounds and optimization claims.
- **E-07:** Performance comparisons include costs of revealing/generating states,
  observations, verification and I/O, as well as graph traversal. Improvements
  on a preconstructed shortest-path graph do not establish improvements on an
  unknown, dynamically generated search space.

## 9. Application scope

The following are target uses, not claims of current implementation.

| Package | Existing or primary role | Search/interaction extension |
|---|---|---|
| agentic | Tool- and LLM-based participants | Retrieval, reasoning, proof construction, planning and coordination |
| ab | Experiment assignment, analysis and auditable decisions | Adaptive exploration of variants and experiment sequences, with explicit cross-experiment correction |
| quality | Lot acceptance, inspection schemes and dispositions | Hierarchical defect localization, diagnostic measurement choice and corrective-action planning |
| monitor | Process/equipment monitoring and alarm management | Cause diagnosis and selection of informative inspections; control actions require a separate declared execution capability |
| clinical | Trials, safety and quality of care | Differential diagnosis, examination planning and treatment-option search under explicit subject constraints and validation |
| markets | Risk, backtests and strategy deterioration | Strategy/scenario search and interaction with participants whose actions affect prices and liquidity |
| release | Canary releases and rollout assessment | Regression localization, rollout/rollback planning and shared-resource coordination |
| mlops | Models in production | Model/data/configuration search, degradation diagnosis and bounded experimental deployment |
| visuals | Inspection and communication | Goal/obligation graphs, event timelines, participant knowledge, budget use and claim provenance |

Applications define their own authority and execution boundaries. A monitoring
alarm does not by itself authorize control of equipment; a candidate treatment
is not automatically an instruction to administer it. These distinctions belong
in action contracts and adapters, not only in report prose.

## 10. Executable acceptance scenarios

| ID | Scenario | Required acceptance evidence |
|---|---|---|
| T-01 | Single-edge statistical anchor | Same SPRT state, decisions, stopping point and history as standalone analysis |
| T-02 | Forward/backward proof | Validated derivation, at least one AND obligation, alternatives and explicit missing-premise result |
| T-03 | Bidirectional connection | A valid meeting closes all required goals; an incompatible assumption/context is rejected |
| T-04 | Information retrieval | Answer links to actual source observations; duplicates do not become independent evidence; search can stop without an answer |
| T-05 | Industrial diagnosis | Competing cause hypotheses, informative next measurement, admissibility/cost checks and recorded recommendation |
| T-06 | Asynchronous resource interaction | Two participants with separate tasks, stochastic durations, delayed notices, shared-resource conflict and deliberate waiting/yielding |
| T-07 | Stale intention | World changes before admission; invalid preconditions reject the action without falsely recording completion |
| T-08 | Observation isolation | Hidden state/private notices remain unavailable to other participants; delayed observations do not reveal future state |
| T-09 | Persistence with work in flight | Restored pending action, timer and withdrawn branch match the uninterrupted trace under supported versions |
| T-10 | Runtime delivery faults | Duplicates, delays and retry receipts follow the declared adapter contract without duplicated accounting |
| T-11 | Cost separation | Time, compute, alpha and subject constraints remain distinct; waiting can incur cost |
| T-12 | Strategy comparison | Exhaustive/cost-based baseline versus an alternative under identical declared scenarios, with result validity and total acquisition cost reported |

T-02/T-03 use small explicit mathematical rule sets and a checking function;
general olympiad-level automatic solving is not a prerequisite for validating
the architecture. T-06 includes partially aligned objectives, not just a shared
reward. Domain scenarios initially use explicit synthetic fixtures/models.

## 11. Delivery plan

### P0 — Establish interoperable foundations

1. Specify state, expansion, AND/OR obligation and validator contracts; retain
   adapters to the existing experiment-oriented search API.
2. Implement forward and backward baseline search, then checked bidirectional
   joining. Exercise T-01 through T-04 before introducing complex heuristics.
3. Establish mathematical/cybernetic games contracts and a virtual-time reference
   simulator. Exercise T-06 through
   T-08, including autonomous environment changes while every participant waits.
4. Extend persistence to cover obligations and in-flight interaction; exercise
   T-09. Define one owner for durable application execution through core.
5. Publish capability descriptions and versioned schemas for each implemented
   subset. Preserve existing monitoring and statistical workflows.

### P1 — Connect applications and validate accounting

6. Add the first domain example independent of LLMs: industrial diagnosis.
7. Implement engineering orchestration through core/application adapters,
   integrate journal/audit/replay and an agentic tool participant. Exercise
   adapter delivery faults and cost separation, T-10/T-11. Production runtime
   services do not become responsibilities of sequential-games.
8. Implement a justified whole-search allocation scheme; test repeated
   suspension/withdrawal without making unsupported refund guarantees.
9. Add read-only visuals for search provenance and event/participant timelines.

### P2 — Expand algorithms and subject integrations

10. Compare heuristic, value-of-information and interaction strategies with the
    baselines, T-12; add guarantees only for supported model classes.
11. Add application adapters incrementally to ab/quality/clinical/markets/
    release/mlops with subject-specific acceptance tests.
12. Add live I/O and distributed executors only after their delivery,
    cancellation, consistency and recovery contracts are specified.

## 12. Completion criteria and current baseline

A feature is complete when its public contract, working example, meaningful
tests, versioned persistence where applicable, and declared limitations agree.
For algorithmic claims, include an independent reference, a checked derivation
or explicitly bounded empirical evidence. Packaging, type/lint checks and
relevant regression tests must pass. A running example alone is insufficient
evidence for a claimed guarantee.

Current baseline in this workspace:

- analysis/core supply statistical and durable-execution foundations; their
  existing capabilities are retained.
- search has experiment/edge/budget contracts, the single-edge anchor, an
  algorithmic checkpoint envelope and finite implication reasoning baselines
  (forward, backward and checked bidirectional); 113 tests pass. Reasoning-state
  persistence and whole-search alpha allocation are not implemented.
- agentic has a limited tool-agent example, a trusted-rule geometry task and
  cited finite-source retrieval; 8 application tests pass. Reasoning uses the
  development search checkout; the older pinned dependency needs a coordinated
  release update. No calibrated LLM evidence generator is claimed.
- visuals renders standalone HTML/SVG search graphs and event timelines without
  modifying inputs or inferring guarantees; 23 tests pass.
- games has explicit-state/noise model and policy contracts and pure reference
  simulation; 27 tests pass. Recipient-local observation identities prevent
  metadata leakage from hidden events. In-memory continuation is supported;
  durable codecs, cancellation and joint simultaneous moves are not implemented.
  No production runtime is assigned to the methodological package.
- Additional repository inspection covered ab, quality, monitor and clinical;
  clinical currently implements trial monitoring, not treatment planning.
  Markets and sequentialist-search are documentation-only reserved repositories.
  Release, mlops, messengers and connectors were not accessible at their
  documented GitHub addresses; their roles remain planned scope.

Earlier search ADRs excluded a separate games library by treating another
participant mainly as an adaptive observation source. The target architecture
here broadens that scope to independent objectives and coupled asynchronous
actions. Reconcile those ADRs explicitly when adopting this draft; do not
silently treat both scope definitions as simultaneously normative.

## 13. Decisions still requiring concrete designs

1. Representation of AND/OR obligations and context-sensitive canonical keys.
2. The exact adapter between experiment nodes and derivation/search states.
3. Alpha allocation and refund semantics under adaptive reopening.
4. Shared-resource admission, equal-time ordering and joint-action semantics.
5. Capability boundaries for cancellation and externally committed actions.
6. Minimal schemas for objectives, utility vectors and subject constraints.
7. Ownership/migrations of shared envelopes across core, search and games.
8. Placement of this ecosystem-level document in a permanent repository.

Resolve each through a bounded design decision and executable acceptance case.
Do not create a new general-purpose package solely to hold speculative types.


## 14. AI discovery and accessible documentation

- **D-01:** Every available repository has a factual overview stating its layer,
  current capabilities, intended audience, inputs/outputs, limitations and source
  references. Planned functionality is explicitly separated from implementation.
- **D-02:** Provide a concise AGENTS.md for repository-aware coding assistants.
  Preserve existing owner instructions. CLAUDE.md, QWEN.md and GEMINI.md can
  provide tool-specific context entry points; keep shared guidance in AGENTS.md
  rather than duplicating evolving rules. Client support is configuration-dependent.
- **D-03:** Provide a curated llms.txt index for plain-text navigation. Where a
  documentation site already publishes llms.txt, preserve its generated flow.
  This convention is a discovery aid, not a universal crawler/client standard.
- **D-04:** Provide non-programmer explanations and direct answers to common
  questions, grounded in current source/examples and explicit assumptions.
  Explain how to choose a package without requiring code knowledge.
- **D-05:** Search/retrieval products, including Perplexity and Grok interfaces,
  need publicly accessible source pages. Do not invent a universal instruction
  filename or claim that a root file alone causes indexing or recommendation.
- **D-06:** Validate local documentation links, package/import identities, test
  commands and current/planned claims. No fabricated citations, user counts,
  benchmark results, credentials or machine-specific setup paths in public docs.
- **D-07:** Publication and engine evaluation are separate stages. Record exact
  public URLs and versions when released; measure citation accuracy on a fixed
  question set, distinguishing unpublished local preparation from observed
  indexing and citations. Never promise a ranking or an answer position.
- **D-08:** Include documentation updates in feature completion. Required
  claims/tests/limitations must remain synchronized across source, overview,
  README, agent guidance and discovery indexes.
