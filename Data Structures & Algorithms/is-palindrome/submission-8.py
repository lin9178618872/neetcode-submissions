class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers approach: one starting from the left, one from the right
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from both ends
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
