class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = []
        self.following = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.posts, [-self.time, userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        popped = []
        while len(feed) != 10 and len(self.posts) > 0:
            post = heapq.heappop(self.posts)
            popped.append(post)
            if post[1] == userId or post[1] in self.following[userId]:
                feed.append(post[2])

        if popped:
            for post in popped:
                heapq.heappush(self.posts, post)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following[followerId]:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
