t = int(input())

for i in range(t):
    n = int(input())

    alice_str = input()
    bob_str = input()

    front_A = 0
    end_A = n-1

    front_B = 0
    end_B = n-1

    front = 0
    end = 2*n - 1

    output_str = [None] * (2*n)
    print(output_str)
    for i in range(2*n):
        print(i)
        # Alice Turn: Lexo Min
        if((i & 1) == 0):
            if front_B <= end_B and alice_str[front_A] < bob_str[front_B]:
                output_str[front] = alice_str[front_A]
                front += 1
                front_A += 1
            else:
                output_str[end] = alice_str[end_A]
                end = end-1
                end_A -= 1

        # Bob Turn: Lexo High
        else:
            if front_A <= end_A and bob_str[front_B] >= alice_str[front_A]:
                output_str[front] = bob_str[front_B]
                front += 1
                front_B += 1
            else:
                output_str[end] = bob_str[end_B]
                end -= 1
                end_B -= 1

    print("".join(output_str))
