# https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
""" 
We have an horizontal number line. On that number line, we have gas stations at positions 
stations[0], stations[1], ..., stations[N-1], where N = size of the stations array. Now, 
we add K more gas stations so that D, the maximum distance between adjacent gas stations,
 is minimized. We have to find the smallest possible value of D. Find the answer exactly 
 to 2 decimal places.

Example 1:

Input:
N = 10
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
Output: 0.50
Explanation: Each of the 9 stations can be added mid way between all the existing 
adjacent stations.
Example 2:

Input:
N = 10
stations = [3,6,12,19,33,44,67,72,89,95]
K = 2
Output: 14.00
Explanation: Construction of gas stations at 86 locations
 """
import math


class Solution:
    def findSmallestMaxDist(self, stations, K):

        # To check that this distance is possible
        def check(distance):

            station_to_add = 0

            for i in range(len(stations)-1):

                station_to_add += math.floor(
                    (stations[i+1] - stations[i]) / distance)

            return station_to_add <= K

        low = 0
        high = stations[-1] - stations[0]

        while high-low > 1e-6:

            mid = (low+high)/2.0

            if check(mid):
                high = mid
            else:
                low = mid

        return high
