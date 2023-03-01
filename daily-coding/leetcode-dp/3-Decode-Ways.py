""" 
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""

""" 
# Recursion TLE
class Solution:
    
    # 226 => (2,2,6), (2,26), (22,6)
    def numDecodings(self, s: str) -> int:
        l = [int(i) for i in s]
        
        if l[0] == 0:
            return 0

        n = len(l)
        # print(l)
    
        # between 1 to 26
        def ways(li,ind):
            if ind == n:
                print(li)
                return 1

            single = l[ind]
            
            if single == 0:
                return 0

            li.append(single)
            count = ways(li,ind+1)

            two_num = 0
            if ind < n-1:
                two_num = (l[ind]*10)+l[ind+1]
            
            count1 = 0

            if two_num in range(1,27):
                li.append(two_num)
                count1 = ways(li,ind+2)
            
            return count+count1
        
        print(ways([],0)) 
"""

# Memorization Accepted
class Solution:
    def numDecodings(self, s: str) -> int:
        
        l = [int(i) for i in s]
        if l[0] == 0:
            return 0
        n = len(l)
        dp = [-1]*n

        def ways(li,ind):
            if ind == n:
                return 1

            if dp[ind] != -1:
                return dp[ind]

            single = l[ind]            
            if single == 0:
                return 0
            li.append(single)
            count = ways(li,ind+1)

            two_num = 0
            if ind < n-1:
                two_num = (l[ind]*10)+l[ind+1]
            count1 = 0
            if two_num in range(1,27):
                li.append(two_num)
                count1 = ways(li,ind+2)
            
            dp[ind] = count+count1
            return dp[ind]

        print(ways([],0))
        return ways([],0)
 

        

obj = Solution()
s = "226"
# s = "60"
# s = "10"
# s = "1204"
obj.numDecodings(s)


""" class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': # if the first character is '0', return 0
            return 0

        n = len(s)
     
        dp = [0] * (n + 1) # create an array of length n + 1 to store number of ways
     
        dp[0], dp[1] = 1, 1 # initialize the first two elements as 1, as there is 1 way to decode empty string and 1 character
     
        for i in range(2, n + 1):
            if s[i - 1] != '0': # if current character is not '0', then it can be a single digit
                dp[i] += dp[i - 1] # add the number of ways to decode the substring ending at i - 1
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'): # if the current and previous character together can be decoded
                dp[i] += dp[i - 2] # add the number of ways to decode the substring ending at i - 2
     
        return dp[n] # return the number of ways to decode the complete string """