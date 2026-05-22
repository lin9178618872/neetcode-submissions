class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        # 按照初始位置，从小到大排序
        cars.sort(key=lambda x: x[0])
        # 计算每辆车到达终点的时间
        time = []
        for i in range(n):
            car = cars[i]
            time.append((target - car[0]) / car[1])
        
        # 使用单调栈计算车队的数量
        # (This part is commented out in the original Java code, so it's also commented out here)
        # stk = []
        # for t in time:
        #     while stk and t >= stk[-1]:
        #         stk.pop()
        #     stk.append(t)
        # return len(stk)

        # 避免使用栈模拟，倒序遍历取递增序列就是答案
        res = 0
        max_time = 0
        for i in range(n - 1, -1, -1):
            if time[i] > max_time:
                max_time = time[i]
                res += 1
        return res

