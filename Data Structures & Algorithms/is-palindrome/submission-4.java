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


            if(Character.toLowerCase(s.charAt(left))!= Character.toLowerCase(s.charAt(right))) return false;
            left++;
            right--;
        }

        return true;
    }
}//n,1
//125