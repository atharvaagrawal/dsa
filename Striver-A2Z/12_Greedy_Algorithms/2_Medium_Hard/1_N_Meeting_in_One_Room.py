# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

""" 
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i 
and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting 
room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
"""


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        meeting = []

        # Sort meeting based on end time
        for i in range(n):
            meeting.append([start[i], end[i], i+1])

        meeting.sort(key=lambda x: x[1])

        res = 0
        end_time = 0

        for i in range(n):
            # If start time is greater than endtime then only take the meeting
            if meeting[i][0] > end_time:
                res += 1
                end_time = meeting[i][1]

        return res
