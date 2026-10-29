# Changelog

## sequentialist-core 0.1.2 — 2026-10-29

The first version published on PyPI. The code of the package is that of
0.1.0; 0.1.1 was tagged but not published.

- The Contributor License Agreement names no court that hears disputes.
- `publish.yml` publishes releases on PyPI by trusted publishing; it can also
  be run by hand for an existing tag.

## sequentialist-core 0.1.0 — 2026-10-28

First version, on sequential-analysis 0.4; tag `v0.1.0`. The code is the same
as at commit 27f7184 (in `packages/core` there), which the other libraries
pinned before the release.

- The repository holds sequentialist-core only, at its root. The other
  libraries moved, with their history, to their own repositories:
  [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) (with
  `@sequentialist/ab-client` and the test vectors) and
  [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality).
- Specs with declarative schemas, every error at once with its JSON pointer,
  normal forms, spec ids, JSON Schema; JSON, and YAML with PyYAML.
- The engine: tasks of several sequential-analysis runs; idempotent intake by
  (source, seq); a journal written before processing; checkpoints; replay after
  a crash giving the uninterrupted task bit for bit; segments; commands with an
  actor and a reason; one writer per task (file locks, version checks); shards.
- Storage in memory, in a directory of JSON files, in SQLite.
- The audit log: decisions and actions chained by SHA-256, with the procedure,
  guarantee, step and history digest behind each; `verify_audit`.
- Reports in JSON and Markdown in which every finding names its guarantee.
- Simulations of whole pipelines, replays on the data's clock, notification
  sinks (log, JSON lines, webhooks), pseudonyms (HMAC-SHA-256).
- The `sequentialist` command, with subcommands added by installed libraries.
