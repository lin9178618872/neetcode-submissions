from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        
        # 初始化 prefix, postfix, 和 res 数组，长度均为 nums_len，初始值全为 1
        # Python 中不需要显式指定类型和初始大小，通过列表推导式实现
        prefix: List[int] = [1] * nums_len
        postfix: List[int] = [1] * nums_len
        res: List[int] = [1] * nums_len

        ## 1. 预生成前缀积数组 (Prefix Products)
        # prefix[i] 存储 nums[0] * nums[1] * ... * nums[i-1]
        
        # prefix[0] 总是 1（左边没有元素）
        # for 循环从 i = 1 开始
        for i in range(1, nums_len):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        ## 2. 预生成后缀积数组 (Postfix Products)
        # postfix[j] 存储 nums[j+1] * nums[j+2] * ... * nums[n-1]
        
        # postfix[nums_len - 1] 总是 1（右边没有元素）
        # for 循环从倒数第二个元素 (nums_len - 2) 开始，到 0 结束
        # range(start, stop, step)
        for j in range(nums_len - 2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]
            
        ## 3. 生成结果 (Result)
        # res[k] = (k 左边的乘积) * (k 右边的乘积) = prefix[k] * postfix[k]
        for k in range(nums_len):
            res[k] = prefix[k] * postfix[k]
            
        return res