def run(tokens):
    stack = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token == "push":
            i += 1
            stack.append(float(tokens[i]))

        elif token == "add":
            if len(stack) < 2:
                return "Error: stack underflow"

            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif token == "pop":
            if not stack:
                return "Error: stack underflow"

            return format_number(stack.pop())
        
        elif token == "sub":
            if len(stack) < 2:
                return "Error: stack underflow"

            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        i += 1


def format_number(x):
    if x == int(x):
        x = int(x)
    return f"{x} + j0"
