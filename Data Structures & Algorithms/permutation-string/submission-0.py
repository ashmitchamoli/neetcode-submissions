class Solution:
    def cmp_dicts(self, d1, d2):
        if len(d1) != len(d2):
            return False

        for k1 in d1:
            if k1 not in d2:
                return False
            
            if d1[k1] != d2[k1]:
                return False
        
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        
        l = 0
        running_freq = defaultdict(int)

        for r in range(len(s2)):
            if s2[r] not in d1:
                l = r+1
                running_freq = defaultdict(int)
                continue
                        
            running_freq[s2[r]] += 1

            while running_freq[s2[r]] > d1[s2[r]]:
                running_freq[s2[l]] -= 1
                l += 1
            
            if self.cmp_dicts(running_freq, d1):
                return True
        
        return False
