# sequentialist-core

Reusable software engineering for the Sequentialist ecosystem. The current
engine turns `sequential-analysis` procedures into durable application tasks
with storage, recovery, audit and reports. Every reported conclusion names the
guarantee declared by its underlying procedure.

## Conceptual framework: the Sequentialist ecosystem

The ecosystem studies sequential decisions: observations arrive, evidence
changes, and a policy chooses whether to continue, act, wait or stop. It separates
three questions within the mathematical and cybernetic methods layer:

| Library | Central question | Responsibility |
|---|---|---|
| [sequential-analysis](https://github.com/andre-a-no/sequential-analysis) | What can we infer from the observations available so far? | Statistical tests, estimation, filtering, prediction and procedure-specific uncertainty guarantees. |
| [sequential-search](https://github.com/andre-a-no/sequential-search) | Which step should we explore next to reach an answer or a goal? | Search and reasoning over alternatives, experiments and rules, with explicit evidence, provenance and resource costs. |
| [sequential-games](https://github.com/andre-a-no/sequential-games) | How do participants pursue their own goals while their actions change a shared environment? | Interaction models for cooperation, competition and partially aligned interests, including asynchronous actions, local information and deliberate waiting. |

These are complementary responsibilities. A participant's policy can use search
to plan and statistical analysis to interpret observations; other participants
continue to act according to their own objectives. This describes how the
methods can be composed. Each package's implementation status is stated
separately below.

The naming convention expresses a further separation into three layers:

| Layer | Packages | Responsibility |
|---|---|---|
| Mathematical and cybernetic methods | `sequential-*`: analysis, search, games | Models, algorithms, explicit state and the assumptions under which a result holds. |
| Reusable engineering platform | `sequentialist-*`, including [core](https://github.com/andre-a-no/sequentialist-core) and [visuals](https://github.com/andre-a-no/sequentialist-visuals) | Durable application execution, storage, recovery, audit and presentation, according to each package's implemented scope. |
| Domain applications | `sequentialist-*`, including [ab](https://github.com/andre-a-no/sequentialist-ab), [quality](https://github.com/andre-a-no/sequentialist-quality), [monitor](https://github.com/andre-a-no/sequentialist-monitor), [clinical](https://github.com/andre-a-no/sequentialist-clinical) and [agentic](https://github.com/andre-a-no/sequentialist-agentic) | Subject-specific goals, workflows, adapters and user-facing decisions built from the methods and engineering components they need. |

Both the engineering platform and applications use the `sequentialist-*`
prefix. The platform is an open family of reusable packages; `core` currently
provides durable tasks built around `sequential-analysis` runs. This organization
does not imply that every combination already has an integration.

Across the ecosystem, state, information available to a decision, randomness,
costs and stopping reasons should be explicit. Evidence, resource expenditure
and real-world effects have separate meanings. Statistical validity, derivability
under supplied rules, properties of an interaction model and reliable execution
each require their own justification; a guarantee in one layer does not
automatically establish a guarantee in another.

### This package's role

**Layer: reusable engineering platform.** Core owns durable application tasks,
journaled intake, checkpoints, storage, audit and reports. Its current engine
executes `sequential-analysis` runs through domain handlers. Statistical methods
stay in `sequential-analysis`; domain decisions stay in application handlers.
Search/game integration requires an explicit adapter. Other reusable engineering
packages, such as visuals, can have their own interfaces and dependencies.

## Package map

This table describes repository source status, not release or deployment status.

| Package | Layer | Current source scope |
|---|---|---|
| [sequentialist-core](https://github.com/andre-a-no/sequentialist-core) | Engineering | Durable tasks, storage, audit and reports |
| [sequentialist-visuals](https://github.com/andre-a-no/sequentialist-visuals) | Engineering | Portable search/event views in its development branch |
| [sequentialist-search](https://github.com/andre-a-no/sequentialist-search) | Engineering, proposed | Planning only; exact responsibilities remain open |
| [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) | Application | A/B experiments; the repository also contains the TypeScript assignment client |
| [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality) | Application | Sequential lot inspection and sampling schemes |
| [sequentialist-monitor](https://github.com/andre-a-no/sequentialist-monitor) | Application | Advisory process/equipment monitoring and alarm management |
| [sequentialist-clinical](https://github.com/andre-a-no/sequentialist-clinical) | Application | Interim trial monitoring and committee reports |
| [sequentialist-agentic](https://github.com/andre-a-no/sequentialist-agentic) | Application | Tool-agent baseline; finite reasoning/retrieval examples in its development branch |
| [sequentialist-markets](https://github.com/andre-a-no/sequentialist-markets) | Application, proposed | Planning only; no implemented market/risk package |

The [ecosystem catalog](docs/ecosystem-catalog.md) provides further context.
The [development roadmap](ROADMAP.md) / [план развития](ROADMAP.ru.md) records
the audited gaps across all twelve repositories, priorities, dependencies and
acceptance criteria. Planned work is distinguished from implemented capabilities.
Additional names mentioned in plans, including `release`, `mlops`,
`messengers` and `connectors`, are proposals rather than implementation claims.

## Installation

Packages have their own dependencies, Python requirements and release status;
check the selected package and revision. Core and the established domain
libraries use the open `sequentialist` namespace.

```
pip install sequentialist-core            # Python 3.8+, depends only on sequential-analysis
pip install "sequentialist-core[yaml]"    # specs in YAML as well as JSON
```

| Module | What it does |
|---|---|
| `spec` | Specs with declarative schemas: every error reported at once with its JSON pointer; a normal form (durations in seconds, timestamps in epoch seconds) and a spec id (SHA-256 of its canonical JSON); JSON Schema for other tools |
| `engine` | Tasks of several streams, each a `Run` of sequential-analysis: idempotent intake by (source, seq), a journal written before processing, checkpoints, replay after a crash, segments (a new run after an alarm or a window), commands of people, one writer per task, shards |
| `storage` | `MemoryStorage`, `FileStorage` (a directory of JSON files), `SQLiteStorage`; `open_storage("files:...")` |
| `audit` | The hash-chained log of decisions and actions, with the evidence behind each: procedure, guarantee, step, history digest; `verify_audit` |
| `report` | Reports in JSON and Markdown; a `Finding` cannot be made without its guarantee |
| `simulate` | Error rates of a whole pipeline by simulation, with Monte Carlo intervals |
| `replay` | Recorded data through the live code, on the data's own clock: the same audit log every time |
| `sinks` | Notifications of decisions: log, JSON lines, webhooks with retries |
| `privacy` | Pseudonyms for identifiers of people (HMAC-SHA-256 under the data owner's key) |

A library implements a `Handler`: it declares its streams and processes
records, the passing of time and commands. The engine does the rest:

```python
from sequentialist.core import Engine, Handler, Record, SQLiteStorage, Stream
from sequential_analysis.procedures import MeanEDetector

class Watch(Handler):
    def __init__(self, spec):
        self.spec = spec

    def streams(self):
        return {"mean": Stream(MeanEDetector(m=self.spec["m"], arl=10000, direction="increase"))}

    def on_record(self, record, ctx):
        event = ctx.step("mean", {"x": record.data["x"]})
        if event is not None and event.terminal:
            ctx.record("decision", "alarm", basis={"t": event.t}, evidence=["mean"])
            ctx.restart("mean", "alarm")

engine = Engine(SQLiteStorage("tasks.db"))
task = engine.create("line-3", "example.watch/1", {"m": 0.2}, Watch({"m": 0.2}))
task.ingest([Record("sensor-7", 0, {"x": 0.18}, time=1793491200.0)])
task.close()
task = engine.open("line-3", Watch)       # restores the checkpoint, replays the journal
```

`sequentialist tasks STORAGE` lists stored tasks; `sequentialist audit
STORAGE TASK` verifies and prints a task's audit log. Installed libraries
add their own subcommands.

**Limits of this version.** The whole state of a task is written at every
checkpoint, so its size (and the cost of a checkpoint) grows with what the
handler keeps; the A/B handler keeps one entry per unit. Locks protect a
task within one host; across hosts the storage must be shared and locked
by other means (Postgres storage is planned).

## What the engine guarantees

* **Idempotent intake**: a record is identified by its source and sequence
  number; sending it again changes nothing.
* **Nothing accepted is lost**: records are journaled before they are
  processed; after a crash the task is restored from its checkpoint and the
  journal is replayed, and the result is the uninterrupted run bit for bit
  (tested on every storage, with crashes at every point that matters).
* **An audit log of every decision**, chained by SHA-256, with the
  procedure, its guarantee, the step and the history digest of
  sequential-analysis that each decision rests on (`sequentialist audit`
  verifies it).
* **One writer per task**, enforced by locks and version checks.

## License

GNU AGPL v3 or a commercial license ([COMMERCIAL.md](COMMERCIAL.md)).
Contributions need the [Contributor License Agreement](CLA.md); see
[CONTRIBUTING.md](CONTRIBUTING.md).

Contact: andrei@hobukob.ru, a.hobukob@gmail.com.

## Reading and repository navigation

Start with the [plain-language overview](docs/overview.md) for use cases, inputs,
outputs and limitations. [llms.txt](llms.txt) indexes the main documentation and
source evidence; [AGENTS.md](AGENTS.md) maps developer entry points and checks.
