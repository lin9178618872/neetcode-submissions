class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        # 按照初始位置，从小到大排序
        #cars.sort(key=lambda x: x[0])
        cars.sort()
        # 计算每辆车到达终点的时间
        time = []
        for i in range(n):
            car = cars[i]
            time.append((target - car[0]) / car[1])
        res = 0
        max_time = 0
        for i in range(n - 1, -1, -1):
            if time[i] > max_time:
                max_time = time[i]
                res += 1
        return res

