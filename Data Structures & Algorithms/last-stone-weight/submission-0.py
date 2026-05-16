import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a < b:
                a = a - b
                heapq.heappush(stones, a)
        if len(stones) == 0:
            val = 0
        else:
            val = -heapq.heappop(stones)
        return val