class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        atlantic_q = deque()
        pacific_q = deque()
        pacific_visit = set()
        atlantic_visit = set()
        
        for r in range(n):
            for c in range(m):
                if r == 0 or c == 0:
                    pacific_q.append((r,c))
                    pacific_visit.add((r,c))
                if r == n-1 or c == m-1:
                    atlantic_q.append((r,c))
                    atlantic_visit.add((r,c))
        #bfs pacific
        while pacific_q:
            for _ in range(len(pacific_q)):
                r,c = pacific_q.popleft()

                neighbours = (r+1,c), (r-1,c), (r,c+1), (r,c-1)
                for (row,col) in neighbours:
                    if (0<= row < n and 0<=col <m and heights[row][col] >= heights[r][c] and (row,col) not in pacific_visit):
                        pacific_visit.add((row,col))
                        pacific_q.append((row,col))

        #bfs atlantic
        while atlantic_q:
            for _ in range(len(atlantic_q)):
                r,c = atlantic_q.popleft()

                neighbours = (r+1,c), (r-1,c), (r,c+1), (r,c-1)
                for (row,col) in neighbours:
                    if (0<= row < n and 0<=col <m and heights[row][col] >= heights[r][c] and (row,col) not in atlantic_visit):
                        atlantic_visit.add((row,col))
                        atlantic_q.append((row,col))
        #intersection
        common_elements = list(set(atlantic_visit) & set(pacific_visit))
        return common_elements