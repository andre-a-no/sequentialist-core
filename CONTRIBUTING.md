# Contributing

Thank you for your interest in sequentialist.

## Contributor License Agreement

sequentialist is offered under the GNU AGPL v3 and under commercial licenses
(see [COMMERCIAL.md](COMMERCIAL.md)). To keep that possible, Novikov
Laboratories LLC must hold the rights needed to license every part of the
code under both. A contribution can therefore be merged only after its
author has signed the Contributor License Agreement ([CLA.md](CLA.md),
Russian and English; a draft until it has been reviewed by a lawyer), sent
to andrei@hobukob.ru. Small fixes of typos in documentation are welcome
without it.

If you write code as part of your job, your employer may own it; in that
case the employer has to sign the CLA as well.

## Development

```
python -m pip install -e . ruff mypy
python -m unittest discover -s tests -t .
ruff check . && mypy
```

- sequentialist-core runs on Python 3.8 and later and needs nothing but
  sequential-analysis (CI checks both, `vermin` checks the language level).
- Statistics belong in sequential-analysis; this package runs procedures,
  it does not compute tests.
- Something goes into sequentialist-core only when at least half of the
  libraries of the family need it; what is in it stays in it.
- New source files start with the SPDX header used throughout the project.
