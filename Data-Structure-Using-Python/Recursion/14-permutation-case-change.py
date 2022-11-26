# Implementation Permutation Case Changes

def solve(ip, op):
    if len(ip) == 0:
        print(op)
        return

    op1 = op + ip[0]
    op2 = op + ip[0].upper()

    ip = ip[1:]

    solve(ip, op1)
    solve(ip, op2)


ip = "ab"
op = ""

solve(ip, op)
