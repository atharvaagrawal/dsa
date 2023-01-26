""" 
Merge two Sorted Arrays Without Extra Space
Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in 
non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains 
the first N elements and modify arr2 so that it contains the last M elements.

Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]

Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]

Explanation:
After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.
"""

# BruteForce: Not inplace
def merge(nums1, m, nums2, n):
    res = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < m and ptr2 < n:
        if nums1[ptr1] < nums2[ptr2]:
            res.append(nums1[ptr1])
            ptr1+=1
        else:
            res.append(nums2[ptr2])
            ptr2+=1
    while ptr1 < m:
        res.append(nums1[ptr1])
        ptr1+=1
    while ptr2 < n:
        res.append(nums2[ptr2])
        ptr2+=1

    print(res)

nums1 = [1,4,8,10]
m = len(nums1)
nums2 = [2,3,9]
n = len(nums2)

merge(nums1,m,nums2,n)