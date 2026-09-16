class Twitter:

    def __init__(self):
        self.t = 0
        self.user_followers = {}
        self.user_tweets = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        heapq.heappush(self.user_tweets[userId], [-self.t, userId, tweetId])
        self.t += 1
        if userId not in self.user_followers:
            self.user_followers[userId] = {userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_followers:
            return []
        res = []
        tweet_list = []

        for followee_id in self.user_followers[userId]:
            if followee_id in self.user_tweets:
                for tweet in self.user_tweets[followee_id]:
                    tweet_list.append(tweet)

        tweet_list.sort(key=lambda entry: entry[0])
        
        for tweet in tweet_list:
            res.append(tweet[2])
            if len(res) == 10:
                return res   
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.user_followers:
            self.user_followers[followerId].add(followeeId)
        else:
            self.user_followers[followerId] = {followerId, followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.user_followers:
            self.user_followers[followerId].discard(followeeId)
        
