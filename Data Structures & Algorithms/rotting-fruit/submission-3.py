class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh_fruit = 0
        counter = 0
        visited = set()



        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        if fresh_fruit == 0:
            return 0
                
        #bfs
        while q:
            wave = len(q)
            for i in range(wave):
                r,c = q.popleft()
                neighbors = (r+1, c), (r-1, c), (r, c+1), (r, c-1)
                for r,c in neighbors:
                    if (0 <= r < n and c >= 0 and c < m and (r,c) not in visited and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r,c))
                        visited.add((r,c))
                        fresh_fruit -= 1

            counter += 1
        if fresh_fruit == 0:
            return counter -1
        else:
            return -1



        