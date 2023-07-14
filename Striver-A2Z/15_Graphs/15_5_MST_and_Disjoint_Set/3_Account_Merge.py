# https://leetcode.com/problems/accounts-merge/description/

""" 
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to 
both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the 
same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the 
rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]


Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""

from typing import List


class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    # Ultimate Parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    # Union by Size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_v] += self.size[ulp_u]

    # Union by Rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)

        accounts.sort()

        # Map Emails to int
        # Connect Emails
        map = dict()
        for i in range(n):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in map:
                    map[mail] = i
                else:
                    ds.unionBySize(i, map[mail])

        mergedMail = [[] for i in range(n)]

        for mail in map:
            node = ds.findUPar(map[mail])
            mergedMail[node].append(mail)

        ans = []
        for i in range(n):
            if len(mergedMail[i]) == 0:
                continue

            mergedMail[i].sort()
            temp = [accounts[i][0]]

            for mail in mergedMail[i]:
                temp.append(mail)

            ans.append(temp)

        return ans
