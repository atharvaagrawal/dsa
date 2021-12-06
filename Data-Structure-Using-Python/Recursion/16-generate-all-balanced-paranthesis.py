# Generate all Balanced Paranthesis

def solve(open_1, close, op):
    if open_1 == 0 and close == 0:
        print(op)
        return

    if open_1 == close:
        op1 = op + "("
        solve(open_1-1, close, op1)

    elif open_1 == 0 and close >= 0:
        op1 = op + ")"
        solve(open_1, close-1, op1)

    else:
        op1 = op + "("
        solve(open_1-1, close, op1)
        op2 = op + ")"
        solve(open_1, close-1, op2)

    return


n = 3
open_1 = 3
close = 3
op = ""

solve(open_1, close, op)
