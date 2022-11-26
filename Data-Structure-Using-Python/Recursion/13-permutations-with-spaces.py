# Implement Permutation with spaces

def permutation(ip, op):
    if len(ip) == 0:
        print(op)
        return

    op1 = op + " " + ip[0]
    op2 = op + ip[0]

    ip = ip[1:]

    permutation(ip, op1)
    permutation(ip, op2)


ip = "ABC"
op = ""
op = ip[0]
ip = ip[1:]
permutation(ip, op)
