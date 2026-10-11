from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = defaultdict(int)
        for x in nums:
            f_map[x] += 1
        
        return [key for (key, _) in sorted(f_map.items(), reverse=True, key=lambda x: x[1])][:k]