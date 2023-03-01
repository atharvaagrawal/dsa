"""
A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities 
(Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated 
with performing an activity each day. The same activity can’t be performed on two consecutive days. 
We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on 
that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn. 

Example:
Input:
n = 3
point= [[1,2,5],[3,1,1],[3,3,3]]
Output:
11

Explanation:
Geek will learn a new move and earn 5 point then on second
day he will do running and earn 3 point and on third day
he will do fighting and earn 3 points so, maximum point is 11.
"""

""" 
Recursion TLE
class Solution:
    def maximumPoints(self, points, n):

        def allWays(points,n,activity):
            if n < 0:
                return 0
            
            # (Running, Fighting Practice, or Learning New Moves)
            firstMove , secondMove, thirdMove = 0,0,0
            if activity != 1:
                firstMove = points[n][0] + allWays(points,n-1,1)
            if activity != 2:
                secondMove = points[n][1] + allWays(points,n-1,2)
            if activity != 3:
                thirdMove = points[n][2] + allWays(points,n-1,3)

            return max(firstMove,secondMove,thirdMove)
        
        print(allWays(points,n-1,0)) 
"""
""" 
# Memorization
class Solution:
    def maximumPoints(self, points, n):
    
        dp = [[-1 for i in range(4)] for j in range(n)]
        
        def allWays(points,n,activity):
            if n < 0:
                return 0
            
            print(n)

            if dp[n][activity] != -1:
                return dp[n][activity]


            # (Running, Fighting Practice, or Learning New Moves)
            firstMove , secondMove, thirdMove = 0,0,0
            
            if activity != 1:
                firstMove = points[n][0] + allWays(points,n-1,1)
            if activity != 2:
                secondMove = points[n][1] + allWays(points,n-1,2)
            if activity != 3:
                thirdMove = points[n][2] + allWays(points,n-1,3)

            dp[n][activity] = max(firstMove,secondMove,thirdMove)
            
            return dp[n][activity]

        print(allWays(points,n-1,0))    
        print(dp)
 """

""" 
# Memorization Top Down

def f(day, last, points, dp):
    if (dp[day][last] != -1):
        return dp[day][last]

    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    for i in range(3):
        if i != last:
            activity = points[day][i] + f(day - 1, i, points, dp)
            maxi = max(maxi, activity)

    dp[day][last] = maxi
    return dp[day][last]

def ninjaTraining(n, points):
    dp = [[-1 for j in range(4)] for i in range(n)]
    return f(n - 1, 3, points, dp)

def main():
    points = [[10,40,70],
              [20,50,80],
              [30,60,90]]

    n = len(points)
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()
"""
""" 
# Tabulation
class Solution:
    def maximumPoints(self, points, n):
    
        dp = [[-1 for i in range(4)] for j in range(n+1)]
        
        # Base Case
        dp[0][0] = max(points[0][1],points[0][2])
        dp[0][1] = max(points[0][0],points[0][2])
        dp[0][2] = max(points[0][0],points[0][1])
        dp[0][3] = max(points[0][0],points[0][1],points[0][2])

        for day in range(1,n):
            for last in range(0,4):
                dp[day][last] = 0
                
                for task in range(0,3):
                    if task != last:
                        point = points[day][task] + dp[day-1][task]

                        dp[day][last] = max(dp[day][last],point)

        
        print(dp[n-1][3])
"""

# Space Optimization
class Solution:
    def maximumPoints(self, points, n):
    
        prev = [-1]*4
        
        # Base Case
        prev[0] = max(points[0][1],points[0][2])
        prev[1] = max(points[0][0],points[0][2])
        prev[2] = max(points[0][0],points[0][1])
        prev[3] = max(points[0][0],points[0][1],points[0][2])

        for day in range(1,n):
            temp = [-1] * 4
            for last in range(0,4):
                temp[last] = 0
                
                for task in range(0,3):
                    if task != last:
                        temp[last] = max(temp[last],points[day][task] + prev[task])
            prev = temp

        print(prev[3])

obj = Solution()

point= [[10,40,70],
        [20,50,80],
        [30,60,90]]
point= [[1,2,5],
        [3,1,1],
        [3,3,3]]
n = len(point)
obj.maximumPoints(point,n)

