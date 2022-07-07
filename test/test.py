def hourglassSum(arr):
    # Write your code here
    row_i = 0
    col_i = 0
    sum = []

    for row in range(3):
        for column in range(3):
            sum.append(arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row + 1][column+1] + arr[row+2][column] +
                       arr[row+2][column+1] + arr[row + 2][column+2])

    print(sum)


arr = [[-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0,  0,  8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
