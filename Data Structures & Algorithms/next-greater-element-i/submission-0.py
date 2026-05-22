class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        # 从右往左
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]

            # 把比当前小的都弹掉
            while stack and stack[-1] < num:
                stack.pop()

            # 栈顶就是右边第一个更大的
            if stack:
                mp[num] = stack[-1]
            else:
                mp[num] = -1

            # 当前元素入栈
            stack.append(num)

        return [mp[x] for x in nums1]