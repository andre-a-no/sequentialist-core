# Contributing

Thank you for your interest in sequentialist.

## Contributions of code are not accepted

sequentialist is offered under the GNU AGPL v3 and under commercial licenses
(see [COMMERCIAL.md](COMMERCIAL.md)). Offering code under both is possible
only while one copyright holder owns all of it, so pull requests with code
or documentation from others are not merged.

Reports of bugs, questions and suggestions are welcome as issues, and by
e-mail to andrei@hobukob.ru.

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
