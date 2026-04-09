class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            #only pop if stack is larger than current value
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                if not stack:
                    width = i
                else: 
                    width = i - stack[-1]  - 1
                area = heights[top] * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
