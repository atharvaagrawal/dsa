class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        rev_str = []
        
        for i in range(len(s)-1,-1,-1):
            rev_str.append(s[i])

        # print('"{}"'.format(rev_str))
        print(rev_str)
        
        
s = Solution()
s.reverseString(["h","e","l","l","o"])