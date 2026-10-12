# ecse428-assignment-a

ECSE 428 Assignment A: `cdc`, a complex-number RPN ("dc") calculator.
Built in Python with Test-Driven Development (pytest).

## Team

| Name                | Student ID |
|---------------------|------------|
| Yanni   | 261233238  |
| Mahad <last name>   | <ID>       |

## Required commands (case-insensitive)

Per Appendix B of the assignment: `PUSH <number>`, `POP`, `ADD`, `SUB`, `MUL`, `DIV`, `DELETE`.

`ABS`, `SIN`, `ASIN`, `COS`, `ACOS`, `SQR` and `SQRT` are required only for 3-student groups, so we do not implement them.

Numbers can be real (`3`, `-2.5`) or complex (`3+j4`, `-1.5-j2`, `j5`, and the spaced form `3 + j 4`).
Output uses the canonical form `RVAL ± jIMAG` (e.g. `5 + j0`, `3 - j1`).
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

*(Available once the command-line interface is implemented.)*

```powershell
python cdc.py push 5 pop
```

## Tests and division of work

Every test ID comes from the assignment's Comprehensive Unit Test Summary Table.
We implement the 20 rows for the required commands (T-PUSH-REAL1 through T-DEL-ERR1).
The rows from T-ABS-REAL1 onward cover the 3-student-only commands and are not implemented.

**Yanni (DONE):**
- [x] T-PUSH-REAL1
- [x] T-POP-ERR1
- [x] T-ADD-REAL1, T-ADD-ERR1
- [x] T-SUB-REAL1, T-SUB-ERR1
- [x] T-MUL-REAL1, T-MUL-ERR1
- [x] T-DIV-REAL1, T-DIV-ERR1

**Mahad (TO DO):**
- [ ] T-PUSH-CPLX1, T-PUSH-CPLX2
- [ ] T-ADD-CPLX1, T-SUB-CPLX1
- [ ] T-MUL-CPLX1, T-DIV-CPLX1
- [ ] T-DIV-ERR2
- [ ] T-DEL-REAL1, T-DEL-CPLX1, T-DEL-ERR1
- [ ] Double check assignment instructions to make sure all is good, nothing else missing.

**Together:** README, PowerPoint, final video.

## TDD workflow

Each increment follows the cycle from the assignment (Kent Beck):
1. Write the smallest failing test (our commit message: `RED: <test id>`).
2. Write the smallest code that passes it (`GREEN: <test id>`).
3. Run the full test suite to confirm no regressions.
4. Refactor only when the suite is fully green.
