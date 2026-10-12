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

        elif token == "mul":
            # multiply the top two numbers and push the result
            if len(stack) < 2:
                return "Error: stack underflow"
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        elif token == "sub":
            # need two numbers to subtract, otherwise underflow
            if len(stack) < 2:
                return "Error: stack underflow"
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "div":
            # a is the number pushed first, b is the top of the stack
            # order matters here: a / b, not b / a
            b = stack.pop()
            a = stack.pop()
            # can't divide by zero
            if b == 0:
                return "Error: division by zero"
            # order matters here: a / b, not b / a

            stack.append(a / b)

        i += 1

def format_number(x):
    if x == int(x):
        x = int(x)
    return f"{x} + j0"
