class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        dq = deque()
        for n in range(len(temperatures)-1, -1, -1):
            #checks for current value is less than smallest deque value
            while dq and temperatures[dq[-1]] <= temperatures[n]:
                dq.pop()            
            if not dq:
                days = 0
            else:
                days = dq[-1]  - n
            dq.append(n)                 
            output[n] = days
       
      
        return output
        