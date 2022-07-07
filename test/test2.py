test_cases = int(input())


def func(n, m, ci):
    sum = 0
    for i in ci:
        sum += i
    candi_each = sum // m

    return sum - m * candi_each


for i in range(test_cases):
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    ci = [int(x) for x in input().split(" ")]

    print('Case #' + str(i+1) + ': ' + str(func(n, m, ci)))
