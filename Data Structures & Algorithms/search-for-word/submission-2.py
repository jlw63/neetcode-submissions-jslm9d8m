class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        output = False
        
        def backtrack(row,col,i):
            nonlocal output

            #boundary of board
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                return
            if board[row][col] != word[i]:
                return
            if i == len(word) -1:
                output = True
                return
            temp = board[row][col]
            board[row][col] = "#"
            i += 1
            #check neigbours
            backtrack(row -1,col,i) #up
            backtrack(row +1,col,i) #down
            backtrack(row ,col -1,i) #left
            backtrack(row ,col+ 1,i) #right

            board[row][col] = temp


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    backtrack(row,col,0)
                    if output:
                        return True

        return output