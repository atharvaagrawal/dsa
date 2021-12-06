# Print 1 to n

def print_n(n):
    if n == 1:
        print(1)
        return

    print_n(n-1)

    print(1)


print_n(7)
