# ecse428-assignment-a

ECSE 428 Assignment A: `cdc`, a complex-number RPN ("dc") calculator in Python, built with TDD (pytest).

**Team:** Yanni Klironomos (261233238), Mahad Haider (261239090)

## Deliverables

- **Code:** `cdc.py`
- **Tests:** `tests/`
- **PowerPoint:** `powerpoint/`
- **Video:** `recording/`

## Setup

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the tests

```powershell
pytest -v
```

## Run the calculator

```powershell
python cdc.py push 5 pop
python cdc.py push 3+j4 push 1+j2 add pop
```