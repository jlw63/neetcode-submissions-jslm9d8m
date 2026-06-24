class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        def dfs(r,c) -> int:
            #outter bounds
            if r < 0 or r >=len(grid) or c < 0 or c >=len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r, c-1)
            

        for r in range(len(grid) ):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cur_size = 0
                    cur_size = dfs(r,c)
                    max_size = max(max_size, cur_size)
        return max_size


        

            