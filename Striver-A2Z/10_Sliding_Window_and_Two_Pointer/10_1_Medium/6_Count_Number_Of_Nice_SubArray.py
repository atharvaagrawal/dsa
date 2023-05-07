""" 
https://leetcode.com/problems/count-number-of-nice-subarrays/description/
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.


Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # 1) Travese j to right and count the odd number of zero
        # 2) If odd_count > k then move i until odd_count becomes equal to k
        def atMost(k):
            i = j = 0
            odd_count = 0
            res = 0

            for j in range(len(nums)):
                if nums[j] % 2 != 0:
                    odd_count += 1

                while odd_count > k:
                    if nums[i] % 2 != 0:
                        odd_count -= 1
                    i += 1

                res = res + (j-i+1)

            return res

        return atMost(k) - atMost(k-1)

    #         public int numberOfSubarrays(int[] A, int k) {
    #     return atMost(A, k) - atMost(A, k - 1);
    # }

    # public int atMost(int[] A, int k) {
    #     int res = 0, i = 0, n = A.length;
    #     for (int j = 0; j < n; j++) {
    #         k -= A[j] % 2;
    #         while (k < 0)
    #             k += A[i++] % 2;
    #         res += j - i + 1;
    #     }
    #     return res;
    # }
