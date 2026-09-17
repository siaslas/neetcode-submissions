class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.t = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = {userId}
        if userId in self.tweets:
            self.tweets[userId].append([self.t, tweetId])
        else:
            self.tweets[userId] = [[self.t, tweetId]]
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            return []

        valid_users = list(self.following[userId])
        candidates = []
        res = []
        followee_cur = []

        for followee in valid_users:
            followee_cur.append(len(self.tweets[followee])-1)
        for i, followee in enumerate(valid_users):
            newest_tweet = self.tweets[followee][followee_cur[i]]
            followee_cur[i] -= 1
            heapq.heappush(candidates, [-newest_tweet[0], followee, newest_tweet[1], i])

        while candidates:
            t, followee, tweet_id, pos = heapq.heappop(candidates)
            res.append(tweet_id)
            if len(res) == 10:
                return res
            if followee_cur[pos] >= 0:
                newest_tweet = self.tweets[followee][followee_cur[pos]]
                followee_cur[pos] -= 1
                heapq.heappush(candidates, [-newest_tweet[0], followee, newest_tweet[1], pos])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
        
