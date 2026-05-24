class Solution:
    def nextGreaterElement(self, nums1, nums2):
        s = []
        maping = {}

        n = len(nums2)

        for i in range(n - 1, -1, -1):
            num = nums2[i]

            while s and s[-1] < num:
                s.pop()

            if s:
                maping[num] = s[-1]
            else:
                maping[num] = -1

            s.append(num)

        res = []

        for x in nums1:
            res.append(maping[x])

        return res