class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_graph = defaultdict(set)
        self.j = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.j,tweetId))
        self.j+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        lst = []
        for i in range(len(self.tweets[userId])-1,-1,-1):
            lst.append(self.tweets[userId][i])
        heapq.heapify(lst)
        print(lst)
        while len(lst) > 10:
            heapq.heappop(lst)
        for following in self.follow_graph[userId]:
            for tweet in self.tweets[following]:
                if len(lst) < 10:
                    heapq.heappush(lst, tweet)
                elif lst[0][0] < tweet[0]:
                    heapq.heappop(lst)
                    heapq.heappush(lst, tweet)
        new_list = []
        while lst:
            new_list.append(lst[0][1])
            heapq.heappop(lst)
        new_list.reverse()
        return new_list
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId  == followeeId:
            return
        self.follow_graph[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_graph[followerId].discard(followeeId)
