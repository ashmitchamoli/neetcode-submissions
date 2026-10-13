class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_yet = (j-i) * min(heights[i], heights[j])

        while i < j:
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
                i += 1
            
            max_yet = max(max_yet, (j-i)*min(heights[i], heights[j]))
        
        return max_yet