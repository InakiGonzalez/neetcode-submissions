class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # i believe the key is to go from row1 -> row2 in the outer loop
        # and col1 to col2 in the inner loop

        total = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                total += self.mat[i][j]
        return total
        '''
        for i range(r1,r2+1)
            for j in range(c1, c2 +1):
                total += self.mat[i][j]
        2 0 1
        1 0 1
        0 3 0
        '''
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)