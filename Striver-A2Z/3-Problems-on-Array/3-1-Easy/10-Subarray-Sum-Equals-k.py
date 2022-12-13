def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    d = dict()
    d[0] = 1
    preSum = 0

    for i in nums:
        preSum += i

        if preSum - k in d.keys():
            ans += d[preSum-k]
        
        d[preSum] = d.get(preSum,0) + 1
    
    return ans