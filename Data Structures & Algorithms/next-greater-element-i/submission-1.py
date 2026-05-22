class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]

            while stack and stack[-1] < num:
                stack.pop()

            if stack:
                mp[num] = stack[-1]
            else:
                mp[num] = -1

            stack.append(num)

        res = []

        for x in nums1:
            res.append(mp[x])

        return res