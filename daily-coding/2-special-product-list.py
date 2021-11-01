'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''


class Solution:
    # Solving using Iteration
    def solve(self, arr):
        arr_res = []  # Resulting array
        res = 1  # for multiplying all elements of array
        n_zero = 0  # for checking number of zeros
        i = 0  # for iterations
        pos = int()  # zero element positon in array

        # loop for multipying all element of array
        for ele in arr:
            res = res * ele

            # if element is zero then increase n_zero and set pos at that index
            if ele == 0:
                n_zero += 1
                pos = i

            # if number of zero is  2 it means complete resulting array is zero
            if n_zero >= 2:
                return list(map(lambda x: 0, arr))
            i += 1

        # if only one element is zero then that postion will contain some value and remaining will be zero
        if n_zero == 1:
            res = 1
            # Calculating multiplication for element with 0
            for j in range(len(arr)):
                if pos != j:
                    res = res * arr[j]
            # Creating array with all 0 and of same length as input
            arr_res = list(map(lambda x: 0, arr))
            # Changing the pos with its value
            arr_res[pos] = res
            print(res, arr)
            return arr_res

        # if there is no zero then calculating the all the element of array
        for ele in arr:
            arr_res.append(res//ele)

        return arr_res


arr = [1, 2, 3, 4, 5]
s = Solution()
print(s.solve(arr))
