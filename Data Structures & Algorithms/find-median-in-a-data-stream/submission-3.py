class MedianFinder:

    def __init__(self):
        self.left = []#max heap
        self.right = []#min heap

        

    def addNum(self, num: int) -> None:
        if not self.right:
            heapq.heappush(self.right, num)
        elif num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        #check length
        while abs(len(self.right) - len(self.left)) >= 2:
            if len(self.left) > len(self.right):
                temp = heapq.heappop(self.left)
                heapq.heappush(self.right, -temp)
            else:
                temp = heapq.heappop(self.right)
                heapq.heappush(self.left, -temp)

        

    def findMedian(self) -> float:
        #check if one array is bigger
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else: #if equal gotta do calculations
            median = (-self.left[0] + self.right[0]) /2
            return median


        