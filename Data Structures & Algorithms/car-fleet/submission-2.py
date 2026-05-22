class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []

        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            pair.append((p, s))

        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            distance = target - p
            time = distance / s
            stack.append(time)

            if len(stack) >= 2:
                last_time = stack[-1]
                prev_time = stack[-2]

                if last_time <= prev_time:
                    stack.pop()

        return len(stack)

