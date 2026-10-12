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







