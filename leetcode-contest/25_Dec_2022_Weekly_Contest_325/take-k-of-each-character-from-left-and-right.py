from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        l = [i for i in s]
        s = set(s)        

        if len(s) != 3 and k >= 1:
            return -1
        
        c = Counter(l)

        if c['a'] < k or c['b'] < k or c['c'] < k:
            return -1
        
        minute = 0
        
        counta = 0
        countb = 0
        countc = 0
        
        start = 0
        end = len(l) -1
        k1 = k
        flag = 0

        while k != 0:
            if counta == countb == countc == k1:
                return minute

            if flag == 0:
                if l[start] == 'a':
                    counta += 1
                elif l[start] == 'b':
                    countb += 1
                elif l[start] == 'c':
                    countc += 1
                start += 1
            else:
                if l[end] == 'a':
                    counta += 1
                elif l[end] == 'b':
                    countb += 1
                elif l[end] == 'c':
                    countc += 1
                end -= 1

            minute += 1      
        
        return minute
