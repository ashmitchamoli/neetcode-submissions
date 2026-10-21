class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        i, j = 0, 1
        seen = {}
        seen[s[0]] = 0
        max_len = 1

        while j < n:
            # shorten until s[j] is not in s[i:j]
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            
            # include s[j] into the substring
            seen[s[j]] = j
            j += 1
            
            max_len = max(max_len, j-i)
        
        return max_len
