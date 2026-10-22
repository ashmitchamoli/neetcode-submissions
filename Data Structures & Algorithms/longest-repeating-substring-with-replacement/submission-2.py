class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0

        f_map = defaultdict(int)
        max_freq = 0
        ans = 0

        for r in range(n):
            f_map[s[r]] += 1
            max_freq = max(max_freq, f_map[s[r]])
            
            if (r-l+1) - max_freq > k:
                f_map[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
                