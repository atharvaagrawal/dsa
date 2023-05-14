# https://leetcode.com/problems/design-twitter/description/

""" 
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
"""


import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.userTweet = defaultdict(list)
        self.userFollow = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.userTweet[userId].append((tweetId, self.time))

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieve 10 Most Recent tweet id
        # Post should be by users who the user follow
        # Tweet must be ordered from most recent to least recent

        def getPost(userId):
            return self.userTweet[userId]

        self_posted = tuple()
        self_posted = getPost(userId)
        users_follow = self.userFollow[userId]

        for i in users_follow:
            self_posted = self_posted + getPost(i)

        # print(self_posted)
        max_heap = []
        for tweetId, time in self_posted:
            # heapq.heappush(max_heap, (-1*dist, [x, y]))
            heapq.heappush(max_heap, (-1*time, tweetId))

        res = []
        for i in range(len(max_heap)):
            if i >= 10:
                break
            res.append(heapq.heappop(max_heap)[1])
        # print(max_heap)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userFollow[followerId]:
            self.userFollow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollow[followerId]:
            self.userFollow[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print('1:', obj.getNewsFeed(1))

obj.follow(1, 2)
obj.postTweet(2, 6)

print('1:', obj.getNewsFeed(1))
obj.postTweet(2, 9)

obj.unfollow(1, 2)
print('1:', obj.getNewsFeed(1))
