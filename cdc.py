def run(tokens):
    stack = []
    i = 0

    while i < len(tokens):
        token = tokens[i].lower()

        if token == "push":
            i += 1
            commands = {"push", "pop", "add", "sub", "mul", "div", "delete"}
            num_tokens = []
            while i < len(tokens) and tokens[i].lower() not in commands:
                num_tokens.append(tokens[i])
                i += 1
            val_str = "".join(num_tokens).replace(" ", "")
            if "j" in val_str:
                if val_str.startswith("j") or val_str.startswith("-j"):
                    val = complex(val_str.replace("j", "") + "j")
                else:
                    r_part, im_part = val_str.rsplit("j", 1)
                    val = complex(float(r_part[:-1]), float(r_part[-1] + im_part))
                stack.append(val)
            else:
                stack.append(float(val_str))
            continue

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

        elif token == "delete":
            if not stack:
                return "Error: stack underflow"
            stack.pop()
        
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


import sys

if __name__ == "__main__":
    cli_tokens = sys.argv[1:]
    
    if cli_tokens:
        result = run(cli_tokens)
        if result is not None:
            print(result)
