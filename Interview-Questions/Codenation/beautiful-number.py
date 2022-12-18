# Beautiful Number in a Range

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

# XOR Sum of the Digits of a Number
def xor_sum_of_digits(n):
    xor_sum = 0
    while n > 0:
        xor_sum = xor_sum ^ (n % 10)
        n = n // 10
    return xor_sum

a = "32"
b = "35"

ct = 0

for num in range(int(a),int(b)+1):
    al = [int(i) for i in str(num)]
    a_min = min(al)
    a_max = max(al)

    sa = xor_sum_of_digits( int(num))
    
    a_avg = (a_min + a_max) // 2

    if sa > a_avg:
        ct+=1

print(ct)

# output the remainder after diving the ct by 10^9+7%
print(ct % (10**9 + 7))