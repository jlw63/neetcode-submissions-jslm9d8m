class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time_to_t = (target - position) / speed
        #current_fleet_time
        pairs = []
        fleet_no = 0
        fleet_time = 0
        for i in range(len(speed)):
            value = [position[i], speed[i]]
            pairs.append(value)
        pairs = self.merge_sort(pairs)
        for cars in pairs:
            pos = cars[0]
            spd = cars[1]
            time = (target - pos)/spd
            if time > fleet_time:
                fleet_time = time
                fleet_no += 1
        return fleet_no
        
        


        
    def merge_sort(self, pairs):
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs)//2
        left = pairs[:mid]
        right = pairs[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)
    
    def merge(self, left, right):
        r_sort = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                r_sort.append(left[i])
                i += 1
            else:
                r_sort.append(right[j])
                j +=1
        r_sort.extend(left[i:])
        r_sort.extend(right[j:])
        return r_sort
        
