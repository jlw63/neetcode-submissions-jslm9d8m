class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        while l <= r:
            k = (l + r) //2
            total_time = 0
            for i in range(len(piles)):
                time = math.ceil(piles[i]/k)
                total_time += time
            if total_time > h:
                l = k + 1
            else:
                r = k -1
        return l

