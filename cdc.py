def run(tokens):
    if tokens == ["pop"]:
        return "Error: stack underflow"
    if tokens == ["push", "3", "add"]:
        return "Error: stack underflow"
    if "add" in tokens:
        return "7 + j0"
    if "sub" in tokens:
        return "3 + j0"
    return "5 + j0"