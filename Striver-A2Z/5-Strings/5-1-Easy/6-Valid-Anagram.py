# https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c1 = Counter(s)
        c2 = Counter(t)

        for i in c1:
            if c1[i] != c2[i]:
                return False
        return True