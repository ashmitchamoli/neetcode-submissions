class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [nums[0]]

        for i in range(1, len(nums)):
            prefix_prod.append(nums[i] * prefix_prod[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            nums[i] *= nums[i+1]
        
        final = []
        for i in range(len(nums)):
            prod = 1
            if i-1 >= 0:
                prod *= prefix_prod[i-1]
            
            if i+1 < len(nums):
                prod *= nums[i+1]
            
            final.append(prod)
        
        return final