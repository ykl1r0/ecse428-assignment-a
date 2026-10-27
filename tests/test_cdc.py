from cdc import run


def test_push_pop_real():  # T-PUSH-REAL1
    assert run(["push", "5", "pop"]) == "5 + j0"

def test_pop_underflow():  # T-POP-ERR1
    assert run(["pop"]) == "Error: stack underflow"

def test_add_real():  # T-ADD-REAL1
    assert run(["push", "2", "push", "5", "add", "pop"]) == "7 + j0"

def test_add_underflow():  # T-ADD-ERR1
    assert run(["push", "3", "add"]) == "Error: stack underflow"

def test_sub_real():  # T-SUB-REAL1
    assert run(["push", "5", "push", "2", "sub", "pop"]) == "3 + j0"

def test_sub_underflow():  # T-SUB-ERR1
    assert run(["sub"]) == "Error: stack underflow"

def test_mul_real():  # T-MUL-REAL1
    assert run(["push", "3", "push", "-2", "mul", "pop"]) == "-6 + j0"

def test_mul_underflow():  # T-MUL-ERR1
    assert run(["mul"]) == "Error: stack underflow"

def test_div_real():  # T-DIV-REAL1
    assert run(["push", "8", "push", "2", "div", "pop"]) == "4 + j0"

def test_div_by_zero():  # T-DIV-ERR1
    assert run(["push", "1", "push", "0", "div"]) == "Error: division by zero"

def test_push_pop_cplx_compact():  # T-PUSH-CPLX1
    assert run(["push", "-2.5-j0.25", "pop"]) == "-2.5 - j0.25"

def test_push_pop_cplx_spaced():  # T-PUSH-CPLX2
    assert run(["push", "3", "+", "j", "4", "pop"]) == "3 + j4"

def test_add_cplx():  # T-ADD-CPLX1
    assert run(["push", "3+j4", "push", "1-j2", "add", "pop"]) == "4 + j2"

def test_sub_cplx():  # T-SUB-CPLX1
    assert run(["push", "3+j4", "push", "1-j2", "sub", "pop"]) == "2 + j6"

def test_mul_cplx():  # T-MUL-CPLX1
    assert run(["push", "1+j2", "push", "3-j4", "mul", "pop"]) == "11 + j2"

def test_div_cplx():  # T-DIV-CPLX1
    assert run(["push", "4+j2", "push", "1+j1", "div", "pop"]) == "3 - j1"

def test_div_by_zero_cplx():  # T-DIV-ERR2
    assert run(["push", "1+j0", "push", "0+j0", "div"]) == "Error: division by zero"

