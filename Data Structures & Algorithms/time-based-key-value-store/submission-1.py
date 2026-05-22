class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]

        left = 0
        right = len(arr) - 1

        res = ""

        while left <= right:

            mid = left + (right - left) // 2

            mid_time = arr[mid][0]
            mid_value = arr[mid][1]

            if mid_time == timestamp:
                return mid_value

            elif mid_time < timestamp:
                res = mid_value
                left = mid + 1

            else:
                right = mid - 1

        return res

