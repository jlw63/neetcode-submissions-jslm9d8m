class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        counter = 0
        q = deque()
        visited = set()
        def bfs():
            while q:
                r,c = q.popleft()
                grid[r][c] = "0"                
                neighbours = (r+1,c), (r-1,c), (r, c+1), (r, c-1)
                for (nr,nc) in neighbours:
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))


        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    q.append((r,c))
                    counter += 1
                    bfs()


        return counter

        