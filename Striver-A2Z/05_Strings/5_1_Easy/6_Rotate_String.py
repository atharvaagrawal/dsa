# https://leetcode.com/problems/rotate-string/description/
def rotateString(self, s: str, goal: str) -> bool:

        if s == goal:
            return True

        for i in range(len(s)):
            t = s[0]
            s = s[1:]
            s = s + t

            if s == goal:
                return True
                
        return False