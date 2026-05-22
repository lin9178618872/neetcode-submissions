class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        left = []
        for i in range(n):
            left.append(-1)

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        right = []
        for i in range(n):
            right.append(n)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        max_area = 0

        for i in range(n):
            left_bound = left[i] + 1
            right_bound = right[i] - 1
            width = right_bound - left_bound + 1
            area = heights[i] * width

            if area > max_area:
                max_area = area

        return max_area
