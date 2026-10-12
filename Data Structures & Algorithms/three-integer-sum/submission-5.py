class Solution:
    def two_sum(self, nums, start, target):
        h = set()
        final = set()
        for i in range(start, len(nums)):
            if target - nums[i] in h:
                final.add((min(nums[i], target - nums[i]),
                              max(nums[i], target - nums[i])))
            
            h.add(nums[i])
        
        return [p for p in final]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = set()
        for i in range(len(nums)):
            for p in self.two_sum(nums, i+1, -nums[i]):
                final.add(tuple(sorted([nums[i], p[0], p[1]])))
            
        return list(list(t) for t in final)