# Changelog

## Unreleased

- The repository holds sequentialist-core only, at its root. The other
  libraries moved, with their history, to their own repositories:
  [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) (with
  `@sequentialist/ab-client` and the test vectors) and
  [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality).
  The code of sequentialist-core is unchanged.
- `publish.yml`: a tag v<version> publishes to TestPyPI (pre-releases) or
  PyPI by trusted publishing, after checking that the tag is the version and
  that the tests pass on the built wheel.

## sequentialist-core 0.1.0 — unreleased

First version, on sequential-analysis 0.4. Version 0.1.0 is the code at
commit 27f7184 (in `packages/core` there), which the other libraries pin
until it is on PyPI.

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
