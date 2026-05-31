class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        col = set()
        negDiag = set() #r -c
        posDiag = set() #r + c
        def backtrack(r):
            if n == r:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                board[r][c] = "Q"
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                backtrack(r+1)
                board[r][c] = "."
                col.discard(c)
                negDiag.discard(r-c)
                posDiag.discard(r+c)
        backtrack(0)
        return res