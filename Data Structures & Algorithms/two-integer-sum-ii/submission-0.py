class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1  # 右移左指针
            else:
                right -= 1  # 左移右指针
#题目是[left+1,right+1]是因为他本来index是0，left + 1 和 right + 1 就是为了把Python默认的“从0开始数”的索引，转换成题目要求的“从1开始数”的索引。
#也就是说如果是0开始