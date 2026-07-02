class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)
        m = len(grid[0])
        q = deque()
        visited = set()
        def bfs() -> int:
            counter = 0
            while q:
                counter += 1
                r,c = q.popleft()
                
                neighbours = (r+1,c), (r-1,c), (r,c+1), (r, c-1)
                for (nr,nc) in neighbours:
                    if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        
                        
            
            return counter




        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited.add((r,c))
                    size = bfs()
                    area = max(size, area)
        return area


                    