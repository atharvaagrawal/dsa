# https://leetcode.com/problems/expression-add-operators/

""" 
Given a string num that contains only digits and an integer target, return all possibilities to insert 
the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression 
evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
"""

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def solve(ind, path, res_so_far, prevNum):
            if ind == len(num):
                if res_so_far == target:
                    res.append(path)
                return

            for i in range(ind, len(num)):

                # Starting with zero
                if i > ind and num[ind] == '0':
                    break
                curr_num = int(num[ind:i+1])

                # if curr index is 0
                if ind == 0:
                    solve(i+1, path+str(curr_num),
                          res_so_far+curr_num, curr_num)
                else:
                    solve(i+1, path+"+"+str(curr_num),
                          res_so_far+curr_num, curr_num)
                    solve(i+1, path+"-"+str(curr_num),
                          res_so_far-curr_num, -curr_num)
                    solve(i+1, path+"*"+str(curr_num), res_so_far -
                          prevNum+prevNum*curr_num, prevNum*curr_num)

        solve(0, '', 0, 0)
        return res


obj = Solution()
num = "123"
target = 6
obj.addOperators(num, target)
