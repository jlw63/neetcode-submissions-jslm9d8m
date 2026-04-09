class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        l = 1
        r = max(piles)
        
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            
            if total_time > h:
                l = k + 1
            else:
                r = k - 1
        
        return l