class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row_set = set()
            for n in i:
                if n == ".":
                    continue
                if n in row_set:
                    return False
                row_set.add(n)
        for n in range(0,9):
            col_set = set()
            for i in range(0,9):
                value = board[i][n]
                if value == ".":
                    continue
                if value in col_set:
                    return False
                col_set.add(value)
        #3x3 boxes check
        for box_row in [0,3,6]:
            for box_col in [0,3,6]:
                box_set = set()
                for r in range(box_row,box_row +3):
                    for c in range(box_col,box_col +3):
                        value = board[r][c]
                        if value == ".":
                            continue
                        if value in box_set:
                            return False
                        box_set.add(value)
                    



        return True

