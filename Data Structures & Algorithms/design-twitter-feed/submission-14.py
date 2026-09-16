class Twitter:

    def __init__(self):
        self.id = 1
        self.t = 0
        self.pq = []
        self.users = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.pq, [-self.t, userId, tweetId])
        self.t += 1
        if userId not in self.users:
            self.users[userId] = {userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        sorted_pq = sorted(self.pq, key=lambda entry: entry[0])
        res = []
        for entry in sorted_pq:
            if entry[1] in self.users[userId]:
                res.append(entry[2])
                if len(res) == 10:
                    return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.users:
            self.users[followerId].add(followeeId)
        else:
            self.users[followerId] = {followerId, followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
        
