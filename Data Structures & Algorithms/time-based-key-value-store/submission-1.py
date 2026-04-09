class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        info = [timestamp, value]
        if key not in self.store:
            self.store[key] = [info]
        else:
            self.store[key].append(info)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            mid = (l + r )//2
            if self.store[key][mid][0] > timestamp:
                r = mid -1
            elif self.store[key][mid][0] < timestamp:
                l = mid + 1
            else:
                return self.store[key][mid][1]
        #if no match
        if r < 0:
            return ""
        else:
            return self.store[key][r][1]



        #if mid is bigger than target then r = mid -1

        #elif mid is smaller than target then l = mid + 1

        #if r is less than target then return empty:
        #if l is more than target return 
        
