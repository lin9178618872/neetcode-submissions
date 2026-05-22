from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        # time 越小表示越新（我们用 0, -1, -2... 这样最小的就是最新）
        self.time = 0

        # 发推记录：
        # tweets[userId] = [[time, tweetId], [time, tweetId], ...]
        self.tweets = defaultdict(list)

        # 关注关系：
        # follows[userId] = set(这个用户关注了谁)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 1) 把这条推存到 userId 的推文列表里
        self.tweets[userId].append([self.time, tweetId])

        # 2) 更新全局时间（下一条推会更“新”）
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 目标：返回 userId 看到的最新 10 条 tweetId
        result = []

        # 小根堆：堆顶是 “最小的 time” => 也就是 “最新的推”
        heap = []

        # 0) 自己必须能看到自己的推，所以把自己也加进关注集合
        self.follows[userId].add(userId)

        # 1) 先把：每个关注的人 的 “最后一条推（最新那条）” 放进堆里
        for who in self.follows[userId]:
            # 如果这个人从来没发过推，跳过
            if len(self.tweets[who]) == 0:
                continue

            # 这个人的最新推在列表最后
            last_index = len(self.tweets[who]) - 1
            t, tid = self.tweets[who][last_index]

            # 堆里放： [time, tweetId, 这个人是谁, 下一条要取的索引]
            # next_index = last_index - 1 表示下一次从他那里取更旧的一条
            heapq.heappush(heap, [t, tid, who, last_index - 1])

        # 2) 不断从堆里弹出“当前全局最新的一条推”
        #    每弹出一条，就把这个人的下一条（更旧的）再塞回堆
        while heap and len(result) < 10:
            t, tid, who, next_index = heapq.heappop(heap)
            result.append(tid)

            # 如果这个人还有更旧的推，就继续加入堆
            if next_index >= 0:
                t2, tid2 = self.tweets[who][next_index]
                heapq.heappush(heap, [t2, tid2, who, next_index - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId 关注 followeeId
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId 取关 followeeId
        # （不需要先判断也行，用 discard 更傻瓜：不在也不会报错）
        self.follows[followerId].discard(followeeId)
