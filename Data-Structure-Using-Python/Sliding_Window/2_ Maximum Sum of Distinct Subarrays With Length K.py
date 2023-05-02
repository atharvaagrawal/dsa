""" 
Maximum Sum of Distinct Subarrays With Length K    
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions. 
"""

from typing import List

# TLE
""" 
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # We can take a window of size k
        # And can calculate the res

        ans = 0
        i = j = 0

        # 1,5,4,2,9,9,9
        # 1,5,4
        #   5,4,2
        c = 0
        window = []

        for j in range(len(nums)):
            window.append(nums[j])
            c += 1
            if c >= k:
                s = set(window)
                if len(s) == k:
                    ans = max(ans, sum(window))
                window.remove(nums[i])
                i += 1
                c -= 1

        return ans
"""

# TLE
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # We can take a window of size k
        # And can calculate the res

        ans = 0
        i = j = 0
        
        # 1,5,4,2,9,9,9
        # 1,5,4
        #   5,4,2
        c = 0
        window = set()

        for j in range(len(nums)):
            if nums[j] not in window:
                if len(window) < k:
                    window.add(nums[j])
                if len(window) == k:
                    ans = max(ans,sum(window))
                    window.remove(nums[i])
                    i+=1
            else:
                window = {nums[j]} 
                i = j
        return ans
"""

""" 
Instead of using a list as a window, we can use two pointers to keep track of the current window. 
This would avoid the overhead of appending and removing elements from the list.

We can also avoid creating a set of the window elements at each iteration. Instead, 
we can keep track of the number of distinct elements in the window and update it as we move the window.

We can use the sliding window technique to avoid computing the sum of the elements in 
the window at each iteration. We can simply subtract the element going out of the window 
and add the element coming in.
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        i = j = 0
        c = 0
        curr = 0
        distinct = 0
        freq = {}

        while j < len(nums):
            # Expand the window
            if nums[j] not in freq or freq[nums[j]] == 0:
                distinct += 1
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            curr += nums[j]
            c += 1
            j += 1

            # Shrink the window
            if c > k:
                if freq[nums[i]] == 1:
                    distinct -= 1
                freq[nums[i]] -= 1
                curr -= nums[i]
                i += 1
                c -= 1

            # Update the answer
            if c == k and distinct == k:
                ans = max(ans, curr)

        return ans
