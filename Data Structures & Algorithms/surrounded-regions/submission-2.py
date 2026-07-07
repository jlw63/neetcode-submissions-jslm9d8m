class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = set()
        q = deque()

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r == 0 or r == n-1 or c == 0 or c == m-1):
                    visited.add((r,c))
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            neighbours = (r+1,c), (r-1,c), (r,c+1), (r,c-1)
            for row,col in neighbours:
                if (0<= row < n and 0<= col < m and (row,col) not in visited  and board[row][col] == "O"):
                    visited.add((row,col))
                    q.append((row,col))
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

        