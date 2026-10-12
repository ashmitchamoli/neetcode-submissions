class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return s[:len(s)//2] == (s[::-1])[:len(s)//2]