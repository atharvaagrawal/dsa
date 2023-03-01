"""
Problem Statement: Given an array of intervals, merge all the overlapping intervals
and return an array of non-overlapping intervals.

Example 1:

Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
 intervals.

Example 2:

Input: [[1,4],[4,5]]

Output: [[1,5]]

Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].
"""

# BruteForce: Got TLE
'''
def overLappingSubInterval(l):
    # Sort the 2d array by start
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j][0] > l[j+1][0]:
                l[j][0], l[j+1][0] = l[j+1][0], l[j][0]
                l[j][1], l[j + 1][1] = l[j+1][1], l[j][1]
    print(l)

    d = dict() # to store start and end

    for i in range(len(l)):
        start, end = l[i][0], l[i][1]

        flag = 0

        for s, e in d.items():
            if start <= e:
                if end > e:
                    d[s] = end

                flag = 1
                break
        if flag == 0:
            d[start] = end

    return [(k,v) for k,v in d.items()]

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[0,4]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

intervals.sort()
print(intervals)
# overLappingSubInterval(intervals)


'''


class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        # Sort the 2d array by start
        l.sort()
        res = []
        s, e = l[0][0], l[0][1]

        for i in range(len(l)):
            start, end = l[i][0], l[i][1]

            if start <= e:
                e = max(end, e)
            else:
                res.append([s, e])
                s, e = start, end

        res.append([s, e])

        return res

