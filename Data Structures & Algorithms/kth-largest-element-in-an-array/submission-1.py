class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []


        for i in nums:
            heapq.heappush(result,i)
            if len(result) > k:
                heapq.heappop(result)

        return result[0]

        
        