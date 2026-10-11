from cdc import run


def test_push_pop_real():  # T-PUSH-REAL1
    assert run(["push", "5", "pop"]) == "5 + j0"

def test_pop_underflow():  # T-POP-ERR1
    assert run(["pop"]) == "Error: stack underflow"



