class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = abs(x)
            y= abs(y)
            if x > y:
                heapq.heappush(stones, -(x - y))
        if not stones:
            return 0
        return -stones[0]
        