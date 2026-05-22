class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # =========================
        # 第一步：把 position 和 speed 一辆车一辆车配起来
        # =========================

        pair = []   # 用来存 (位置, 速度)

        for i in range(len(position)):
            p = position[i]     # 第 i 辆车的位置
            s = speed[i]        # 第 i 辆车的速度
            pair.append((p, s)) # 放进列表

        # 现在 pair 长这样：
        # [(位置1, 速度1), (位置2, 速度2), ...]



        # =========================
        # 第二步：按位置从大到小排序（离终点近的在前面）
        # =========================

        pair.sort(reverse=True)



        # =========================
        # 第三步：准备一个栈（用来存每辆车到终点的时间）
        # =========================

        stack = []



        # =========================
        # 第四步：一辆一辆车处理
        # =========================

        for p, s in pair:

            # 这辆车到终点还要走多远
            distance = target - p

            # 需要多少时间到终点
            time = distance / s

            # 把时间放进栈
            stack.append(time)



            # =========================
            # 第五步：判断会不会追上前面的车
            # =========================

            # 如果栈里至少有两辆车
            if len(stack) >= 2:

                # 当前车时间
                last_time = stack[-1]

                # 前一辆车时间
                prev_time = stack[-2]

                # 如果当前车更快 或 一样快
                # 说明会追上前车，变成一个车队
                if last_time <= prev_time:

                    # 把当前车弹掉（合并成前面的车队）
                    stack.pop()



        # =========================
        # 最后：栈里剩多少时间 = 多少车队
        # =========================

        return len(stack)
