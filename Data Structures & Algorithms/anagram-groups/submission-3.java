public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {//字符串变数组字符
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());//putifabsent如果所指定的 key 已经在 HashMap 中存在，返回和这个 key 值对应的 value, 如果所指定的 key 不在 HashMap 中存在，则返回 null。
            res.get(key).add(s);//// 这行代码的作用是向 key1 关联的 List 中添加 value1
        }
        return new ArrayList<>(res.values());
    }
}
//Time complexity: O(m*n),O(m)