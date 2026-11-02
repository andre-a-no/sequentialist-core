# What sequentialist-core does

Languages: [English](overview.md) · [Русский](overview.ru.md)

`sequentialist-core` is a Python library for running long-lived applications of
sequential statistics with recoverable state and an explainable decision record.
It belongs to the ecosystem's **software-engineering platform**. The statistical
algorithms live in `sequential-analysis`; domain packages decide what an
experiment, inspection, alarm or intervention means.

## When it is useful

Use it when a stream-processing application must continue after a restart,
recognize repeated records, and show why it produced a decision. Typical users
are developers building A/B testing, lot inspection or monitoring applications.
It is a library to embed, not a hosted service or a ready-made dashboard.

| Input | Processing responsibility | Output |
|---|---|---|
| A validated task specification and a domain Handler | Declare streams and bind sequential-analysis procedures | A task with identifiable configuration |
| Records carrying source, sequence and data | Journal intake, enforce ordering/deduplication and advance the handler | Updated state and domain decisions |
| Time notifications or explicit commands | Invoke the handler and record resulting actions | Auditable transitions |
| Stored task state and journal | Restore state and replay accepted input | A continued task |
| Findings and their supporting evidence | Retain the procedure's declared guarantee | JSON/Markdown reports and notifications |

The library supplies `MemoryStorage`, `FileStorage` and `SQLiteStorage`.
Applications provide their Handler and input adapters. The [README example](../README.md)
shows a monitoring Handler using a mean-change detector.

## A workflow without writing application code

If you are evaluating a system built with this library, ask its developer or
assistant for the task's specification, recorded inputs, report and audit
verification result. Read the reported conclusion together with its named
guarantee and assumptions. An audit log explains which computation produced a
decision; it does not establish that the input data or subject model is correct.

For an existing store, the installed CLI can list tasks with
`sequentialist tasks STORAGE` and inspect a task with
`sequentialist audit STORAGE TASK`. `STORAGE` is the application's configured
storage URL; task creation and domain commands are supplied by the application.
Do not invent a store path or run a new intervention merely to inspect a report.
An assistant can explain exported JSON/Markdown without executing an application.

This repository alone does not provide a web interface, a clinical workflow,
a production deployment, or an automatic decision maker for every domain.

## What is implemented and what remains limited

The checked-out source implements specifications, tasks, journaling,
checkpoint/replay, the three storage backends, audit, reporting, simulation
helpers, pseudonyms and notification sinks. The package version is defined in
[version.py](../src/sequentialist/core/version.py); installation requirements are
in [pyproject.toml](../pyproject.toml). Published-package availability is not
established by a source version or an installation example.

Important limits of this version:

- The whole task state is written at a checkpoint. Its size grows with state
  retained by the Handler.
- Locks protect a task on one host. The package does not supply a distributed
  database/locking solution or a PostgreSQL backend.
- Statistical guarantees are inherited from the selected procedures and their
  assumptions. Durable storage and a hash-chained audit do not strengthen them.
- Webhook retry behavior does not imply exactly-once physical effects at an
  external destination.
- Search/game application adapters are an ecosystem direction, not a claim that
  this engine already implements generic proof search or game orchestration.

## Frequently asked questions

**Is this the statistics package?** No. Use `sequential-analysis` for procedures;
use this package to build an application around them.

**Is core the entire engineering platform?** No. `sequentialist-visuals` has a
separate reusable visualization responsibility; other demonstrated engineering
needs can have their own packages. Domain applications form another layer.

**Does an audit prove that a recommendation is correct?** It verifies the
recorded lineage under the implementation's contract. Subject validity and
statistical assumptions remain separate questions.

**Can it resume after a crash?** The engine restores checkpoints and replays its
journal. The exact supported behavior and failure boundaries are exercised by
the engine/storage tests; external side effects need their own adapter contract.

**Can I use it without LLMs?** Yes. Handlers and procedures do not require an LLM
or `sequentialist-agentic`.

## Sources and further reading

- [README and executable example](../README.md)
- [Task engine](../src/sequentialist/core/engine.py)
- [Storage implementations](../src/sequentialist/core/storage)
- [Audit verification](../src/sequentialist/core/audit.py)
- [Reporting](../src/sequentialist/core/report.py)
- [Tests](../tests) and [CI commands](../.github/workflows/tests.yml)
- [Developer navigation](../AGENTS.md) and [contribution contract](../CONTRIBUTING.md)

[llms.txt](../llms.txt) is a curated navigation index. It does not guarantee
indexing, retrieval or interpretation by any particular search engine or model.
