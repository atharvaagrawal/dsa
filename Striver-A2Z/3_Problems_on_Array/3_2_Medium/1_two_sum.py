# https://leetcode.com/problems/two-sum/description/s

def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(len(nums)-1):
            sum = nums[i]
            for j in range(i+1,len(nums)):
                if target == (sum+nums[j]):
                    return [i,j]


def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i