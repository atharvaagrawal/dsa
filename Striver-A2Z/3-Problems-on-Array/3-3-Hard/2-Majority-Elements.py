""" 
TC: O(n)
SC: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []

        for val,coun in c.items():
            if coun > len(nums)//3:
                res.append(val)
        
        return res
"""

#  (Extended Boyer Moore’s Voting Algorithm)
# n/3 majority elements
# TC: O(n)
# SC: O(1)

def majorityElement(nums):
    n = len(nums)
    if n == 0:
        return []
    if n == 1:
        return nums
    if n == 2:
        return list(set(nums))

    count1 = 0
    count2 = 0
    first = nums[0]
    second = nums[0]

    for i in range(n):
        if nums[i] == first:
            count1 += 1
        elif nums[i] == second:
            count2 += 1
        elif count1 == 0:
            first = nums[i]
            count1 = 1
        elif count2 == 0:
            second = nums[i]
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    for i in range(n):
        if nums[i] == first:
            count1 += 1
        elif nums[i] == second:
            count2 += 1
    res = []
    if count1 > n//3:
        res.append(first)
    if count2 > n//3:
        res.append(second)
    return res


 