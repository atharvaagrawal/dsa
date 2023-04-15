""" 
https://practice.geeksforgeeks.org/problems/reverse-a-stack/1

Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}
"""

class Solution:
    def reverse(self,st): 

        def insertAtBottom(st,top):
            if len(st) == 0:
                st.append(top)
                # print(st,top)
                return
            
            val = st.pop()
            insertAtBottom(st,top)
            st.append(val)
            # print(st)

        def solve(st,n):
            if n == 0:
                return
            
            top = st.pop()
            solve(st,n-1)
            insertAtBottom(st,top)
        n = len(st)
        solve(st,n)

obj = Solution()
st = [3,2,1,7,6]
st = [4, 5, 7]
print("Before Reverse:",st)
obj.reverse(st)
print("After Reverse:",st)
