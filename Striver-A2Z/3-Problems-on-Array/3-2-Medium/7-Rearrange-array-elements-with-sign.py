# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        res = []
        j = 0
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res