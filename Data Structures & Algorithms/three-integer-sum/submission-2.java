class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 结果列表
        List<List<Integer>> result = new ArrayList<>();
        
        // 排序数组
        Arrays.sort(nums);
        
        // 遍历数组，固定第一个数 nums[i]
        for (int i = 0; i < nums.length - 2; i++) {
            // 如果当前数字与前一个数字相同，跳过以避免重复结果
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // 使用双指针查找两个数，使得三数之和为零
            int left = i + 1; // 左指针初始化为 i 之后的第一个数
            int right = nums.length - 1; // 右指针初始化为数组末尾
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // 如果三数之和为零，将结果加入列表
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // 移动左指针，跳过重复元素
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    
                    // 移动右指针，跳过重复元素
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    // 移动指针，寻找新的组合
                    left++;
                    right--;
                } else if (sum < 0) {
                    // 如果三数之和小于零，移动左指针使和增大
                    left++;
                } else {
                    // 如果三数之和大于零，移动右指针使和减小
                    right--;
                }
            }
        }
        
        // 返回结果列表
        return result;
    }
}//on^2,on
//15