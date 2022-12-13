# https://takeuforward.org/data-structure/subarray-with-given-sum/
def maxSubArray(nums):
        max_so_far = nums[0]
        max_end = 0
        arr = []
        res = []
        for i in nums:
            max_end = max_end + i
            arr.append(i)

            if max_so_far < max_end:
                max_so_far = max_end
                res = arr

            if max_end < 0:
                max_end = 0
                arr = []

        print(max_so_far)
        print(res)

nums = [1, 7, 3, 9]
nums = [-2,1,3,4,-5,6]
maxSubArray(nums)
