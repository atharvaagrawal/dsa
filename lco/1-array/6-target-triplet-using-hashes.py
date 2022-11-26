# Target Triplet
'''
Array: [5,20,12,45,7,15,24,4]
Sum of 3 Element of Array: 34 [15,7,12]
'''


def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()

        print('\n\n i:', i)
        print('s:', s)

        curr_sum = sum - A[i]

        print('curr_sum:',)

        for j in range(i + 1, arr_size):

            print('\n j:', j)
            print('s:', s)
            print(curr_sum - A[j])
            print((curr_sum - A[j]) in s)
            print(len(s))
            if (curr_sum - A[j]) in s:

                print("Triplet is", A[i],
                      ", ", A[j], ", ", curr_sum-A[j])
                return True
            s.add(A[j])

    return False


# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
find3Numbers(A, arr_size, sum)
