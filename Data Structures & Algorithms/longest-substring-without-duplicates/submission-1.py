class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        i, j = 0, 1
        seen = defaultdict(int)
        seen[s[0]] = 1
        max_len = 1

        while j < n:
            # shorten until s[j] is not in s[i..j]
            while i < j and seen[s[j]] > 0:
                seen[s[i]] -= 1
                i += 1
            
            # include s[j] into the substring
            seen[s[j]] += 1
            j += 1
            
            max_len = max(max_len, j-i)
        
        return max_len
