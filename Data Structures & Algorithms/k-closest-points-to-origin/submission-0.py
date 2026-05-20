class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = [] 


        for i in points:
            x = i[0]
            y = i[1]
            distance = -(x**2 + y**2)
            val = [distance,[x,y]]
            heapq.heappush(result , val)
            if len(result) > k:
                heapq.heappop(result)
        final = []
        for i in result:
            top = i[1]
            final.append(top)
        return final
        

        
        
        