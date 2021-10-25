# Bit Manipulation

def bit_division(dividend, divisor):
    if divisor == 0:
        return "Error"

    if dividend < divisor:
        return "Special Case"

    if dividend == divisor:
        return 1

    if divisor == 1:
        return dividend

    qu = 1
    te = divisor

    while te < dividend:
        te = te << 1  # Left Shift
        qu = qu << 1

    if te > dividend:
        qu = qu >> 1
        te = te >> 1
        return qu + bit_division(dividend-te, divisor)

    return qu


print(bit_division(40, 5))
print(bit_division(40, 4))
