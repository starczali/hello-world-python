# hello-world-python

A small Python CLI that prints a greeting in several languages, with an optional time-of-day mode.

## Setup (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If activation is blocked by execution policy, run once per session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Run

```powershell
python hello.py
python hello.py --name Andrei --lang ro
python hello.py --name Andrei --time-aware
```

Flags:

- `--name` — name to greet (default: `World`)
- `--lang` — `en`, `es`, `fr`, `ro`, or `de` (default: `en`)
- `--time-aware` — greet based on the current hour instead of language

## Test

```powershell
pytest
```
