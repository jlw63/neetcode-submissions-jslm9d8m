class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        for n in range(len(height)):
            max_left = 0

            for i in range(0, n+1):
                max_left = max(max_left,height[i])
            max_right = 0
            for i in range(n, len(height)):
                max_right = max(max_right, height[i])
            i_water = min(max_left, max_right) - height[n]
            if i_water > 0:
                total_water += i_water

        return total_water

        