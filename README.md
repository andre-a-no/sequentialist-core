# sequentialist-core

The common layer of the sequentialist libraries: applications of sequential
statistics built on
[sequential-analysis](https://github.com/andre-a-no/sequential-analysis).
The statistics live in sequential-analysis; this package turns its
procedures into applications that run for months, survive crashes and can
be audited, and every conclusion they report names its guarantee
(`exact`, `asymptotic`, `model`, `approximate` or `none`), as the procedure
behind it states it.

| Library | Repository | Status |
|---|---|---|
| `sequentialist-core` | this one | 0.1.0: specs, the checkpointed engine, storage, audit log, reports, simulations |
| `sequentialist-ab`, `@sequentialist/ab-client` (npm) | [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) | 0.1.0: the engine of an A/B testing platform |
| `sequentialist-quality` | [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality) | 0.1.0: sequential acceptance sampling of lots |
| `sequentialist-monitor` | [sequentialist-monitor](https://github.com/andre-a-no/sequentialist-monitor) | planned: equipment, processes and energy |
| `sequentialist-markets` | [sequentialist-markets](https://github.com/andre-a-no/sequentialist-markets) | planned: risk, backtests, strategy decay |
| `sequentialist-clinical` | [sequentialist-clinical](https://github.com/andre-a-no/sequentialist-clinical) | planned: trials, drug safety, quality of care |
| `sequentialist-release`, `sequentialist-mlops` | | planned: canary releases, models in production |

The libraries are installed separately and share the `sequentialist`
namespace. None is on PyPI yet.

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
Contributions of code are not accepted; issues are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).

Contact: andrei@hobukob.ru, a.hobukob@gmail.com.
