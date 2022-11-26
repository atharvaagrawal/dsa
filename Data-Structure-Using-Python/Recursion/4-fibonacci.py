# Program to implement fibonacci Series
# 0 1 1 2 3 5 8 13

def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def fibo(n):
    for i in range(n):
        print(Fibonacci(i), end=" ")


fibo(5)
