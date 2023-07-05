# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

""" 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)

        n2 = len(nums2)

        arr = nums1
        arr.extend(nums2)

        arr.sort()

        # Even Number
        if (n1+n2) % 2 == 0:
            return (arr[len(arr)//2-1] + arr[(len(arr)//2)]) / 2.0
        else:
            return arr[len(arr)//2]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = n1

        medianPos = (n1+n2+1)//2

        while low <= high:

            cut1 = (low+high)//2
            cut2 = medianPos - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1, r2))/2.0

            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1

        return 0.0
