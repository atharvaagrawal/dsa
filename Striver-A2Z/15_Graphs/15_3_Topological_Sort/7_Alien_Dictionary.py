# https://practice.geeksforgeeks.org/problems/alien-dictionary/1

""" 
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output 
will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 
Example 1:

Input: 
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is 
'b', 'd', 'a', 'c' Note that words are sorted 
and in the given language "baa" comes before 
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Example 2:

Input: 
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.
"""


class Solution:
    def findOrder(self, alien_dict, N, K):

        adj_l = [[] for _ in range(K)]

        # Number Represent
        num = dict()

        for i in range(K):
            num[chr(97+i)] = i

        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]

            # Find differentiating alphabet added to adj list
            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    adj_l[num[s1[j]]].append(num[s2[j]])
                    break

        # AdjList Created Now just sort it
        queue = []

        # Calculate Indegree
        indegree = [0]*K

        for i in range(K):
            for j in adj_l[i]:
                indegree[j] += 1

        # Add all indegree 0
        for i in range(K):
            if indegree[i] == 0:
                queue.append(i)

        res = ''
        while queue:
            vertex = queue.pop(0)

            res = res + str(chr(vertex+97))

            # Reduce indegree of others
            for i in adj_l[vertex]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return res
