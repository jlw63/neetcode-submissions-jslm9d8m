class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n  = len(matrix[0]) # coloumns
        m = len(matrix)     # rows
        l = 0
        r = m*n -1


        while l <= r:
            mid = (l + r )//2
            row = mid // n
            col = mid % n
            k = matrix[row][col]
            if k > target:
                r = mid - 1


            elif k < target:
                l = mid + 1
            else:
                return True
        return False
        