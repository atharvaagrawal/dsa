from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def solve(divisor):
            s = 0

            for i in nums:
                s += math.ceil(i/divisor)

            return s

        low = 1
        high = max(nums)
        ans = float('inf')

        # Find smallest divisor which is less than or
        # equal to threshold

        while low <= high:
            mid = (low+high) // 2

            res = solve(mid)

            print(res, mid, ans)

            if res > threshold:
                low = mid+1
            else:
                ans = min(mid, ans)
                high = mid-1

        return ans


obj = Solution()

nums = [44, 22, 33, 11, 1]
threshold = 5

# nums = [1, 2, 5, 9]
# threshold = 6
print(obj.smallestDivisor(nums, threshold))
