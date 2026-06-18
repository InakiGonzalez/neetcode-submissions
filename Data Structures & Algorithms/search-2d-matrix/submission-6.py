class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        row = 0
        top = 0
        bottom = ROWS -1
        while top <= bottom:

            r = (top + bottom) // 2

            if target > matrix[r][-1]:
                top = r + 1

            elif target < matrix[r][0]:
                bottom = r -1
            else: 
                row = r
                break
        if not (top <= bottom):
            return False

        l = 0
        r = COLS - 1
        while l <= r:
            m  = (l+r) // 2

            if  target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


       