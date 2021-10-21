'''
Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''


def subset(s, index, holder):

    if index == len(s):
        print('\n3)', holder, end=" ")  # string or ARRAY
        print("\n")
        arr.append(holder)
        return

    print('1) s:', s, 'index:', index, 'holder:', holder)
    subset(s, index+1, holder + s[index])

    subset(s, index+1, holder)
    print('2) s:', s, 'index:', index, 'holder:', holder)


# main
arr = []
s = "123"
index = 0
holder = ""
subset(s, index, holder)
print("ARR:", arr)
