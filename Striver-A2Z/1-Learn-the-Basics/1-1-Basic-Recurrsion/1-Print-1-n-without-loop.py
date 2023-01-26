# Print 1-N without Loop

def printLoop(n):
    if n == 0:
        return

    printLoop(n - 1)
    print(n, end=" ")


n = int(input("Enter a number:"))

printLoop(n)
