""" 
# https://leetcode.com/problems/hand-of-straights/description/


Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""


import heapq
from queue import Queue
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """ 
        hand = [1,2,3,6,2,3,4,7,8]
        sorted = [1,2,2,3,3,4,6,7,8]
        We need to check the consecutiveness also
        """

        if len(hand) % groupSize != 0:
            return False

        # Put element in heap
        min_heap = [val for val in hand]
        heapq.heapify(min_heap)
        q = Queue()

        while min_heap:
            val = heapq.heappop(min_heap)
            k = groupSize
            k -= 1

            # Now find the val+1
            # if not found put it in Queue
            while k != 0:
                if not min_heap:
                    return False

                tmp = heapq.heappop(min_heap)

                if tmp == val:
                    q.put(tmp)
                elif tmp == val+1:
                    k -= 1
                    val = tmp
                else:
                    return False

            while not q.empty():
                heapq.heappush(min_heap, q.get())

        return True
