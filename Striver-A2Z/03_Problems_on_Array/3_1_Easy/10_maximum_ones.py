def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0

        for i in nums:
            if i == 1:
                c +=1
            else:
                m = max(c,m)
                c = 0
        m = max(c,m)
        return m  