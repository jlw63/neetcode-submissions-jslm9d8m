class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        q = deque()
        freshCount = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshCount += 1
        if freshCount == 0:
            return 0

        #bfs
        counter = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] != 2:
                    grid[r][c] = 2
                    freshCount -= 1
                
                neighbours = (r+1,c), (r-1,c), (r,c+1),(r,c-1)
                for (row,col) in neighbours:
                    if (0<= row < n and 0 <= col < m and grid[row][col] == 1 and (row,col) not in visited):
                        visited.add((row,col))
                        q.append((row,col))
            counter += 1
        if freshCount > 0:
            return -1
        return counter -1
        