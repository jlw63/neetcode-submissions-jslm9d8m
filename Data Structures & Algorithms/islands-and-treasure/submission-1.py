class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
        while q:
            r,c = q.popleft()
            direction = [[1,0], [-1,0], [0,1], [0, -1]]

            for dr, dc in direction:
                row,col = r + dr, c + dc
            
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == inf:
                    grid[row][col] = grid[r][c]  + 1
                    q.append([row,col])