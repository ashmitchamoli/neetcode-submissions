from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = defaultdict(int)
        for x in nums:
            f_map[x] += 1
        
        f_map = {k: v for (k, v) in sorted(f_map.items(), reverse=True, key=lambda x: x[1])}
        ans = list(f_map.keys())[:k]

        return ans