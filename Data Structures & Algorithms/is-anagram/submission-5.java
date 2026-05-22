public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char currentChars = s.charAt(i); // 获取当前字符
            int currentCounts = countS.getOrDefault(currentChars, 0); // 获取当前字符的计数，默认是0
            countS.put(currentChars, currentCounts + 1); // 更新计数并存入map
            char currentChart = t.charAt(i); // 获取当前字符
            int currentCountt = countT.getOrDefault(currentChart, 0); // 获取当前字符的计数，默认是0
            countT.put(currentChart, currentCountt + 1); // 更新计数并存入map
        }
        return countS.equals(countT);
    }
}
//o(n),o(n)
