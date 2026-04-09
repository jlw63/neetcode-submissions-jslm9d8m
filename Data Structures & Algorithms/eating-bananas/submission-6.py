class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (r +l )//2
            time = 0
            for i in piles:
                rate = math.ceil(i/mid)
                time += rate
            if time <= h:
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
            

            