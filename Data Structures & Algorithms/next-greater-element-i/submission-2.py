class Solution:
    def nextGreaterElement(self, nums1, nums2):
        s = []
        mp = {}

        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]

            while s and s[-1] < num:
                s.pop()

            if s:
                mp[num] = s[-1]
            else:
                mp[num] = -1

            s.append(num)

        res = []

        for x in nums1:
            res.append(mp[x])

        return res