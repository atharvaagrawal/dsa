# https://leetcode.com/problems/reverse-words-in-a-string/description/
def reverseWords(self, s: str) -> str:
        rev = ""
        flag = 0
        s = s.strip()
        flag = 0
        org = ""
        s = s + ' '
        for i in range(0,len(s)):

            if s[i] == ' ' and flag == 0:
                org = rev + ' ' + org  
                flag = 1 
                rev = ""
            elif s[i] != ' ':
                rev = rev + s[i]
                flag = 0
        org = org.strip()
        return org