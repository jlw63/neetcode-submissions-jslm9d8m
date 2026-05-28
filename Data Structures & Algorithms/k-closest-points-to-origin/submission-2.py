class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for i in points:
            x = i[0]
            y = i[1]
            distance = ((x) **2 + (y) **2)
            heapq.heappush(heap, (-distance,i))
        #(x1 - x2)^2 + (y1 - y2)^2
            if len(heap) > k:
                heapq.heappop(heap)
        for i in heap:
            output.append(i[1])
        return output


        