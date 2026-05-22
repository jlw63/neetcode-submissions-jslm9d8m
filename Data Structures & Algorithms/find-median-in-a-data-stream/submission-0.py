class MedianFinder:

    def __init__(self):
        #larger numbers go here - minheap
        self.minheap = []
        #smaller numbers go here - max heap
        self.maxheap= []
        

    def addNum(self, num: int) -> None:
        #if minheap is empty add first val
        if not self.minheap:
            heapq.heappush(self.minheap, num)
            return
        #start compare
        #compare new number with minheap first index
        if num > self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap, -num)
        #if smaller than minheap first index add to max heap
        #else add to min heap
        #check difference of the 2 length of the heap
        minlength = len(self.minheap)
        maxlength = len(self.maxheap)
        if minlength > maxlength:
            if(minlength - maxlength) == 2:
                temp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -temp)        
        else:
            if(maxlength - minlength) == 2:
                temp = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -temp)  
        #if difference of 2 then remove the right most value and add it to the other index??

        

    def findMedian(self) -> float:
        maxlength = len(self.maxheap)
        minlength = len(self.minheap)
        if maxlength == minlength:
            return (-self.maxheap[0]+ self.minheap[0])/2

        elif maxlength > minlength:
            return -self.maxheap[0]
        
        else:
            return self.minheap[0]

        #check length of both, 
        #if both lengths are equal must take min and max of both heaps and find average

        #if one is larger, find the larger heap then retrun the first index of that heap

        
        