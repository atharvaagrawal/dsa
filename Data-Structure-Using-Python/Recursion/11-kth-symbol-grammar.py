# Kth Symbol in Grammar

def solve(n, k):
    if n == 1 and k == 1:
        return 0

    mid = pow(2, n-1)//2

    if k <= mid:
        return solve(n-1, k)
    else:
        return abs(~solve(n-1, k-mid))


print(solve(1, 1))
print(solve(2, 1))
print(solve(2, 2))
print(solve(3, 1))
print(solve(3, 3))
