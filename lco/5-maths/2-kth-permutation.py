# Factorial
def factorial(n):
    if n is 0 or n is 1:
        return 1

    return n * factorial(n-1)


def kth_permutation_helper(v, k, result):
    # if v is not there or k is not there
    if not v:
        return

    n = len(v)
    b_count = factorial(n-1)
    select = (k-1) // b_count

    result += str(v[select])

    del v[select]

    k = k - (b_count * select)

    kth_permutation_helper(v, k, result)


def kth_permutation(n, k):
    v = list(range(1, n+1))

    result = []
    kth_permutation_helper(v, k, result)
    return ''.join(result)


n = 3
k = 4

print(kth_permutation(n, k))
