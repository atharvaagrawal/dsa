# Pascal Trianle
'''
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
'''


# Pascal Triangle Using Recursion
def pp(line_number):
    if line_number == 0:
        return [1]
    else:

        line = [1]  # Start of the array

        last_line = pp(line_number - 1)

        for i in range(len(last_line)-1):
            line.append(last_line[i] + last_line[i+1])

        line += [1]  # End of the array
    return line


# Printing Pascal Triangle using Recurssion
def pascal_triangle(n):
    ptri = {}

    # Creating a pascal triangle using Hashmaps
    for i in range(1, n+1):

        # Creating an array equal to position of pascal triangle with all zero
        arr = list(map(lambda x: 0, range(i)))

        arr[0], arr[-1] = 1, 1  # Assiging 1 1 at start and end
        ptri[i] = arr  # Adding array into hashmaps

        if i > 2:
            for j in range(i-2):
                if i > 2:
                    ptri[i][j+1] = ptri[i-1][j] + ptri[i-1][j+1]  # Pascal Sum

    # Printing the Pascal Triangle
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')

        for j in range(i+1):
            print(ptri[i+1][j], end='  ')
        print('')


pascal_triangle(10)
print(pp(5))
