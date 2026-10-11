from cdc import run


def test_push_pop_real():  # T-PUSH-REAL1
    assert run(["push", "5", "pop"]) == "5 + j0"