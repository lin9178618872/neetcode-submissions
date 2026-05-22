class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        res[0] = 1;//不是第一个数
//从左往右
        int curr = nums[0];//从0开始
        for(int i = 1; i < nums.length; i++) {
            res[i] = curr;
            curr *= nums[i];
        }
//从右往左，保留最后一位
        curr = nums[nums.length - 1];
        for(int i = nums.length - 2; i >= 0; i--){
            res[i] *= curr;
            curr *= nums[i];
        }

        return res;
    }
}
//O(n),O(n)
//238