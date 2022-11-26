# Permutation Letter Case

def solve(ip, op):
    if len(ip) == 0:
        print(op)
        return

    if ip[0].isnumeric():
        op1 = op + ip[0]
        ip = ip[1:]

        solve(ip, op1)
    else:
        op1 = op + ip[0].lower()
        op2 = op + ip[0].upper()

        ip = ip[1:]

        solve(ip, op1)
        solve(ip, op2)


ip = "a1B2"
op = ""

solve(ip, op)
