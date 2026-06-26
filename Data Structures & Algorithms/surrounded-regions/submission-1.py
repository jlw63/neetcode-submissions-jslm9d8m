class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        q = deque()
        visited = set()
        for r in range(n):
            for c in range(m):
                if (r == 0 or r == n-1 or c == 0 or c == m-1) and board[r][c] == "O":
                    q.append((r,c))
                    visited.add((r,c))
        #bfs
        while q:
            r,c = q.popleft()
            neighbours = (r-1,c), (r+1,c), (r,c+1),(r,c-1)
            for (r,c) in neighbours:
                if (0 <= r < n and 0 <= c < m and board[r][c]== "O" and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))

        for r in range(n):
            for c in range(m):
                if (r,c) not in visited and "O":
                    board[r][c] = "X"
        


        