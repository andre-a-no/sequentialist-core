# Repository guide

Read [CLAUDE.md](CLAUDE.md) for the existing owner guidance. Preserve that file;
this guide adds navigation and commands, not a second set of owner rules.

`sequentialist-core` is the reusable software-engineering layer. Statistical
methods belong to `sequential-analysis`; subject decisions belong to application
handlers. Do not treat recovery/audit guarantees as statistical validity.

## Source map

- [README.md](README.md): supported behavior and a working Handler example.
- [docs/overview.md](docs/overview.md): plain-language use cases and limits.
- [engine.py](src/sequentialist/core/engine.py): task lifecycle, records and Handler integration.
- [storage](src/sequentialist/core/storage): memory, file and SQLite storage.
- [audit.py](src/sequentialist/core/audit.py), [report.py](src/sequentialist/core/report.py): decision lineage and findings.
- [spec.py](src/sequentialist/core/spec.py), [schema.py](src/sequentialist/core/schema.py): declarative input contracts.
- [tests](tests), [CI](.github/workflows/tests.yml): executable regression requirements.
- [CONTRIBUTING.md](CONTRIBUTING.md), [pyproject.toml](pyproject.toml): contribution and compatibility contracts.

## Development checks

Run from this repository root using the intended environment:

```bash
python -m pip install -e '.[yaml]' ruff mypy vermin==1.9.0
python -W error::ResourceWarning -m unittest discover -s tests -t .
ruff check .
mypy
vermin --no-tips --violations -t=3.8- src tests
```

Python runtime support is 3.8+, while the configured type-checking interpreter
target is separate. Preserve the PEP 420 `sequentialist` namespace. Before
describing a new capability as implemented, inspect the source and relevant
test; project plans and historical release notes are not execution evidence.
