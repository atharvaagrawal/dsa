# Print N-Bit Binary Number's having more 1's than 0's for any prefix

def solve(one, zero, n, op):
    if n == 0:
        print(op)
        return

    if one == zero:
        op1 = op + "1"
        one += 1
        n -= 1
        solve(one, zero, n, op1)
        return

    op1 = op + "1"
    solve(one+1, zero, n-1, op1)

    op2 = op + "0"
    solve(one, zero+1, n-1, op2)


n = 5
op = ""
solve(0, 0, n, op)
