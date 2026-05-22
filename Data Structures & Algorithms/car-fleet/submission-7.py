class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #组合
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        cars.sort()
        # 计算每辆车到达终点的时间
        time = []
        for i in range(n):
            car = cars[i]
            time.append((target - car[0]) / car[1])#car[0]为刚才的位置，[1]为速度
        
        #计算多少个fleet队
        res = 0
        max_time = 0
        for i in range(n - 1, -1, -1):
            if time[i] > max_time:
                max_time = time[i]
                res += 1
        return res

