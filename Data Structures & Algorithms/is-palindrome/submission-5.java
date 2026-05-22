class Solution {
    public boolean isPalindrome(String s) {
        if(s == null || s.length() == 0) return true;

        int left = 0;
        int right = s.length() - 1;

        while(left < right){
            while (left < right) {
                if (!Character.isLetterOrDigit(s.charAt(left))) {
                    left++;
                    } else {
                        break; // 找到有效字符后跳出循环
                        }
                        }
            while (left < right) {
                if (!Character.isLetterOrDigit(s.charAt(right))) {
                    right--;
                    } else {
                        break; // 找到有效字符后跳出循环
                        }
                        }


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
}//n,1
//125