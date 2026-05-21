class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = {}
        self.follows = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer = self.timer + 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.timer, tweetId])





    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        following = self.follows.get(userId, set())
        following.add(userId)
        for user in following:
            if user in self.tweets:
                for (timestamp, tweetId) in self.tweets[user]:
                    heapq.heappush(heap, (-timestamp, tweetId))

        while len(result) < 10 and heap:
            timestamp, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        
        return result




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        
        
            



        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

        
        
