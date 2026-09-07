class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        for f in self.following[userId] | set([userId]):
            if f in self.posts:
                index = len(self.posts[f]) - 1
                time, tweetid = self.posts[f][index]
                heap.append([time, f, tweetid, index-1])

        heapq.heapify(heap)
        while len(res) < 10 and heap:
            time, f, tweetid, index = heapq.heappop(heap)
            res.append(tweetid)
            if index >= 0:
                time, tweetid = self.posts[f][index]
                heapq.heappush(heap, [time, f, tweetid, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)