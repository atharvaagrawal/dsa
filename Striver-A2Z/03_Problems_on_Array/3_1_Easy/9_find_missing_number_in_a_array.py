from collections import defaultdict

def missingNumber(nums):
        d = {}
        d = defaultdict(lambda: 0,d)

        for i in nums:
            d[i] = 1
        
        # print(d)
        
        for i in range(len(nums)+1):
            # print(i,d[i])
            if d[i] != 1:
                return i