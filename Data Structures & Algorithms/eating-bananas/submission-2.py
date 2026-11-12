class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        while i < j:
            mid = (i+j)//2

            h_need = 0
            for pile in piles:
                h_need += pile//mid + (pile%mid > 0)
                if h_need > h:
                    break
            
            if h_need > h:
                i = mid+1
            elif h_need <= h:
                j = mid
        
        return (i+j)//2

        