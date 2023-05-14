""" 
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth 
smallest element in the given array. It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

Example 2:
Input:
N = 5
arr[] = 7 10 4 20 15
K = 4
Output : 15
Explanation :
4th smallest element in the given 
array is 15.
"""

# Got TLE
""" 
from queue import PriorityQueue

class MaxHeapElement:
    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority

class Solution:
    def kthSmallest(self, arr, l, r, k):
        q = PriorityQueue()

        for i in arr:
            q.put(MaxHeapElement(i))

            if q.qsize() > k:
                q.get()

        return q.get().priority 
"""




import heapq
class Solution:
    # As Smallest use the MAX Heap

    def kthSmallest(self, arr, l, r, k):
        pq = []
        n = len(arr)

        for i in range(n):
            heapq.heappush(pq, -1*arr[i])

            if i >= k:
                heapq.heappop(pq)

        return -1*pq[0]


obj = Solution()
arr = [7, 10, 4, 3, 20, 15]
l = 0
r = len(arr) - 1
k = 3
print(obj.kthSmallest(arr, l, r, k))  # 7
