def singleNumber(self, nums: List[int]) -> int:
        d = {}
        d = defaultdict(lambda: 0,d)

        for i in nums:
            d[i] +=1
        
        for i in d.keys():
            if d[i] == 1:
                return 