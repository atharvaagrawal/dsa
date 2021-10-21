# Convert Decimal Number to Binary Number

def decBin(n, res):
    if n == 1:
        res.append(1)
        return ''.join(map(str, reversed(res)))

    res.append(n % 2)

    return decBin(int(n/2), res)


def decimal_to_binary(val):
    if val <= 1:
        return str(val)
    else:
        return decimal_to_binary(val // 2) + decimal_to_binary(val % 2)


n = int(input("Enter a Decimal Number:"))
print(decBin(n, []))
print(decimal_to_binary(n))
