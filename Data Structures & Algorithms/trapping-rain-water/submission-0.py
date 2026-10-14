class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [-1]
        for i in range(1, n):
            pre.append(max(pre[i-1], height[i-1]))
        
        suf = [-1]*n
        for i in range(n-2, -1, -1):
            suf[i] = max(suf[i+1], height[i+1])
        
        ans = 0
        for i in range(1, n-1):
            ans += max(0, min(pre[i], suf[i]) - height[i])
        
        return ans