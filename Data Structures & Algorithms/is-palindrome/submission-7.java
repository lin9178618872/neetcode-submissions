class Solution {
    public boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) return true;

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // 移动 left 指针
            while (left < right) {
                if (!Character.isLetterOrDigit(s.charAt(left))) {//isLetterOrDigit检查字符是否为字母或数字。
                    left++;
                } else {
                    break; // 找到有效字符后跳出循环
                }
            }

            // 移动 right 指针
            while (left < right) {
                if (!Character.isLetterOrDigit(s.charAt(right))) {
                    right--;
                } else {
                    break; // 找到有效字符后跳出循环
                }
            }

            // 比较字符
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
//n,1
//125