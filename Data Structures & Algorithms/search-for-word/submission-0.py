class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        output = False


        def backtrack(r,c, index):
            nonlocal output
            #basecase
            if r >= len(board) or r <0 or c >= len(board[0]) or c <0:
                return
            if board[r][c] != word[index]:
                return
            if index == len(word) -1 :
                output = True
                return
            temp = board[r][c]
            board[r][c] = "#"
            #neighbour exploration
            backtrack(r-1,c,index+1)
            backtrack(r+1,c,index+1)
            backtrack(r,c-1,index+1)
            backtrack(r,c+1,index+1)

            board[r][c] = temp

        #loop thru board to find start
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    backtrack(r,c,0)
                    if output:
                        return True
    

        return output