# ecse428-assignment-a

ECSE 428 Assignment A: `cdc`, a complex-number RPN ("dc") calculator.
Built in Python with Test-Driven Development (pytest).

## Team

| Name              | Student ID |
|-------------------|------------|
| Yanni  | 261233238      |
| Mahad | <ID>       |

## Supported commands (case-insensitive) as per assignment instructions for groups of 2

`PUSH <number>`, `POP`, `ADD`, `SUB`, `MUL`, `DIV`, `DELETE`

Numbers can be real (`3`, `-2.5`) or complex (`3+j4`, `3 + j 4`, `j5`).
Output uses canonical form `RVAL ± jIMAG` (e.g. `5 + j0`, `3 - j1`).
Errors: `Error: stack underflow`, `Error: division by zero`, invalid token.

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
```

## Division of work

Each test ID maps to the Comprehensive Unit Test Summary Table in the assignment instructions. Since our group has two students, we implement the base commands only (everything up to T-DEL-ERR1).

**Yanni**:
- T-PUSH-REAL1: push/pop (real)
- T-POP-ERR1: pop on empty stack
- T-ADD-REAL1, T-ADD-ERR1
- T-SUB-REAL1, T-SUB-ERR1
- T-MUL-REAL1, T-MUL-ERR1
- T-DIV-REAL1, T-DIV-ERR1
- T-DEL-REAL1, T-DEL-ERR1

**Mahad**:
- T-PUSH-CPLX1: complex push (compact)
- T-PUSH-CPLX2: complex push (spaced)
- Canonical output formatting, invalid token handling, case-insensitivity
- T-ADD-CPLX1, T-SUB-CPLX1
- T-MUL-CPLX1, T-DIV-CPLX1
- T-DIV-ERR2: division by complex zero
- T-DEL-CPLX1

**Together:** project setup, README, PowerPoint, final video.

## TDD workflow

Every increment follows the Kent Beck TDD cycle:
1. Write one failing test (commit `RED: <test id>`).
2. Write the minimum code to pass (commit `GREEN: <test id>`).
3. Run the full suite to confirm no regressions.
4. Refactor only when the suite is fully green (commit `REFACTOR: <description>`).

Screenshots of each step can be collected for the PowerPoint walkthrough.