class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        q = deque()


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        distance = 0
        while q:
            for _ in range(len(q)):

                r,c = q.popleft()
                if grid[r][c] != 0:
                    grid[r][c] = distance
                neighbours = (r+1,c), (r-1,c),(r,c+1), (r, c-1)
                for row, col in neighbours:
                    if (0 <= row < n and 0 <= col < m and (row,col) not in visited and grid[row][col] == 2147483647):
                        visited.add((row,col))
                        q.append((row,col))
            distance += 1
