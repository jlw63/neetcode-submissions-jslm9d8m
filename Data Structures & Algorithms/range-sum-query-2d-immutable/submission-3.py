class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefix = [[0] * (col + 1) for _ in range(row+ 1)]
        for i in range(row):
            for j in range(col):
                self.prefix [i+1][j+1] = matrix[i][j] + self.prefix[i][j+1] + self.prefix[i+1][j] - self.prefix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        big_box = self.prefix[row2+1][col2+1]
        top_strip = self.prefix[row1][col2+1]
        left_strip = self.prefix[row2+1][col1]
        corner = self.prefix[row1][col1]
        return big_box - top_strip - left_strip + corner

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)