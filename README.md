# DevOps-CI-Demo (Python)

A tiny Python example to demonstrate CI with GitHub Actions.

## How to run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app.py
```

You should see `Hello CI`.
