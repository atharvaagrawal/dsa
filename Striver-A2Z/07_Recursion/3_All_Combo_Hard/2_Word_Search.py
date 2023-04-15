""" 
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if the word exists in the grid. 
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: 
[
["A", "B", "C", "E"], 
["S", "F", "C", "S"],
["A", "D", "E", "E"]
] 
word = "ABCCED"
Output: true
Explanation: We can easily find the given word in the matrix.

Example 2:
Input:
[
["A", "B", "C", "E"],
["S", "F", "C", "S"],
["A", "D", "E", "E"]
]
word = "ABCB"
Output: false
Explanation:  There is no such word in the given matrix. 
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # i = row
        # j = col

        row_len = len(board)
        col_len = len(board[0])
        n = len(word)

        def solve(i, j, ind, s):
            if ind == n:
                # print(s)
                return True
            if i < 0 or i >= row_len or j < 0 or j >= col_len or board[i][j] == '!':
                return False
            if board[i][j] != word[ind]:
                return False

            s += board[i][j]

            # To Prevent Using Same Character
            c = board[i][j]
            board[i][j] = '!'

            # rowwise # colwise # row backward # col upward
            res = solve(i+1, j, ind+1, s) or solve(i, j+1, ind+1,
                                                   s) or solve(i-1, j, ind+1, s) or solve(i, j-1, ind+1, s)

            board[i][j] = c

            return res

        ind = 0

        # First search the first character
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    if solve(i, j, ind, ''):
                        return True

        return False
