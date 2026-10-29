class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        n = len(s)
        sCount = defaultdict(int)
        tCount = defaultdict(int)
        
        for c in t: tCount[c] += 1

        ans = []
        have, need = 0, len(tCount)
        for r in range(n):
            sCount[s[r]] += 1

            if s[r] in tCount and tCount[s[r]] == sCount[s[r]]:
                have += 1

            while have == need:
                # print(len(tCount), len(sCount))
                if ans == [] or r-l < ans[1] - ans[0]:
                    ans = [l, r]
                
                sCount[s[l]] -= 1
                if s[l] in tCount and tCount[s[l]] > sCount[s[l]]:
                    have -= 1

                l += 1
        
        return "" if ans == [] else s[ans[0]:ans[1]+1]
                