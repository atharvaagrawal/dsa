from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n//2

        left = 0
        right = n - 1

        while left <= right and right < n:
            # print(left,right,mid)

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1

            if nums[mid] < target:
                left = mid+1

            if left > right:
                return -1

            mid = (left+right) // 2
        return -1
