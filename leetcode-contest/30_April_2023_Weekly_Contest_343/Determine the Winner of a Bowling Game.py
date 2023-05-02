# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        p1 = 0
        p2 = 0
        c1 = 0
        c2 = 0

#         for i in player1:
#             if c1 > 0:
#                 p1 += 2*i
#                 c1-=1
#             else:
#                 p1 += i

#             if i == 10:
#                 c1 +=2

#         for i in player2:
#             if c2 > 0:
#                 p2 += 2*i
#                 c2-=1
#             else:
#                 p2 += i

#             if i == 10:
#                 c2 +=2

        for i in range(len(player1)):
            if c1 > 0:
                p1 += 2*player1[i]
                c1 -= 1
            else:
                p1 += player1[i]

            if c2 > 0:
                p2 += 2*player2[i]
                c2 -= 1
            else:
                p2 += player2[i]

            if player1[i] == 10:
                c1 = 2
            if player2[i] == 10:
                c2 = 2

        # print(p1,p2)
        if p1 == p2:
            return 0
        if p1 > p2:
            return 1
        if p2 > p1:
            return 2
