class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        left, right = 0, len(arr) - 1
        res = ""  # 记录符合条件的值

        # 使用模板：寻找 <= timestamp 的最大 timestamp
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                res = arr[mid][1]      # 有效候选，继续找更大的
                left = mid + 1
            else:
                right = mid - 1

        return res
