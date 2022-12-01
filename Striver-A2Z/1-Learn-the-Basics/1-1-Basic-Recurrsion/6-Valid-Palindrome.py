# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(self, s: str) -> bool:
        rev = ""
        s = s.lower()
        org = ""
        # Removing the spaces and special character
        for i in s:
            if((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >=48 and ord(i) <= 57)):
                org +=i
        
        rev = org[::-1]

        if( rev == org):
            return True
        return False

s = "A man, a plan, a canal: Panama"
if(isPalindrome(s)):
    print("Palindrome")    
else:
    print("Not Palindrome")