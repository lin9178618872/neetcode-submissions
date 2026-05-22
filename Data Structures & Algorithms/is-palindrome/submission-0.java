class Solution {
    public boolean isPalindrome(String s) {
    // 转换字符串为小写，并移除所有非字母数字字符
    s = s.toLowerCase().replaceAll("[^a-z0-9]", "");

    // 初始化两个指针，i 指向字符串开始位置，j 指向字符串末尾位置
    int i = 0;
    int j = s.length() - 1;

    // 当 i 指针不超过 j 指针时，继续循环
    while (i <= j) {
        // 如果字符不相等，返回 false
        if (s.charAt(i) != s.charAt(j)) {
            return false;
        }

        // 移动指针
        i++;
        j--;
    }

    // 字符串是回文，返回 true
    return true;    
    }
}//O(n),o(n)
