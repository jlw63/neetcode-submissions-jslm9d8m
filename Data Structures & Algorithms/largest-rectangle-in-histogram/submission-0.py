class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]: 
                top = stack.pop()
                width = i if not stack else i - stack [-1] -1

                area = width * heights[top]
                max_area = max(max_area, area)
            stack.append(i)
        return max_area