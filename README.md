# data-quality-checks

![CI](https://github.com/AdenAbbas/data-quality-checks/actions/workflows/ci.yml/badge.svg)

Small Python data-validation functions with pytest tests and a GitHub Actions CI pipeline.

## Functions

| Function | What it checks |
|---|---|
| `check_required_fields(record, required)` | Returns the list of required fields that are missing or blank |
| `is_positive_number(value)` | Value is an int/float greater than zero (booleans rejected) |
| `is_valid_email(value)` | Value looks like `name@domain.tld` |

## Run locally

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows; use `source .venv/bin/activate` on macOS/Linux
pip install -r requirements-dev.txt
ruff check . && ruff format --check .
pytest -v
```

## CI

`.github/workflows/ci.yml` runs on every push and pull request, on Python 3.11 and 3.12:

1. Check out the code
2. Set up Python (with pip caching)
3. Install pinned dependencies from `requirements-dev.txt`
4. Lint with ruff (`ruff check` + `ruff format --check`)
5. Run the pytest suite

If any step fails, the run fails and the commit is marked red on GitHub.
