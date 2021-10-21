class Solution:
    def solve(self, nums, k):
        nums.sort()
        return self.target_double(nums, k, 0, len(nums)-1)

    def target_double(self, arr, k, start, end):
        if start >= end:
            return False

        if arr[start]+arr[end] == k:
            print(arr[start], arr[end])
            return True
        elif arr[start]+arr[end] > k:
            return self.target_double(arr, k, start, end-1)
        elif arr[start]+arr[end] < k:
            return self.target_double(arr, k, start+1, end)


s = Solution()
print(s.solve([15, 0, 3, 2], 15))
