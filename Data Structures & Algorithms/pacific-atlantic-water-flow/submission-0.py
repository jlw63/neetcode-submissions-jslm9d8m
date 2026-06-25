class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        pacific_q = deque()
        atlantic_q = deque()
        def bfs(q)->List[List[int]]:
            visited = set()
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                cur_r, cur_c = r,c
                neighbours = (r+1,c), (r-1,c), (r,c+1), (r, c-1)
                for (r,c) in neighbours:
                    if (0 <= r < n and 0 <= c < m and grid[cur_r][cur_c] <= grid[r][c] and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
            return visited


        
        #pacific edge
        for r in range(n):
            pacific_q.append((r,0))
            atlantic_q.append((r,m-1))
        for c in range(m):
            pacific_q.append((0,c))
            atlantic_q.append((n-1,c))

        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)

        u = [list(cell) for cell in (pacific_reachable).intersection(atlantic_reachable)]
        return u
        

