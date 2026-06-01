class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        visit = set()
        island = 0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                rows, cols = q.popleft()
                direction = ([1,0],[-1,0],[0,1],[0,-1])
                for dr, dc in direction:
                    r,c = rows +dr, cols+dc
                    if ((r) in range(row) and
                        (c) in range(col) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1


        return island