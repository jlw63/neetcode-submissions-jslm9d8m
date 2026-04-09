class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max_area = 0
        while l < r:
            width = r - l
            length = min(heights[l], heights[r])
            current_area = width * length
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1            
            else:
                r -=1
                l +=1
            if current_area > max_area:
                max_area = current_area
        return max_area

        