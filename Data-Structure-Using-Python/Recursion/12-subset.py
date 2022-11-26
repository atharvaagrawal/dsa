# Print Subset

def solve(ip, op):
    if len(ip) == 0:
        print(op, end=" ")
        return

    op1 = op
    op2 = op

    op2 = op2 + str(ip[0])
    ip = ip[1:]

    solve(ip, op1)
    solve(ip, op2)


ip = "ABC"
op = ''

solve(ip, op)
