class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)

        while i <= j:
            mid = (i + j) // 2

            if mid >= len(nums): break

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        
        return -1
        