def run(tokens):
    stack = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token == "push":
            i += 1
            val_str = tokens[i]
            if "j" in val_str:
                r_part, im_part = val_str.rsplit("j", 1)
                val = complex(float(r_part[:-1]), float(r_part[-1] + im_part))
                stack.append(val)
            else:
                stack.append(float(val_str))

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
    if isinstance(x, complex):
        r = int(x.real) if x.real.is_integer() else x.real
        im = int(x.imag) if x.imag.is_integer() else x.imag
        sign = "+" if im >= 0 else "-"
        return f"{r} {sign} j{abs(im)}"
    if x == int(x):
        x = int(x)
    return f"{x} + j0"
