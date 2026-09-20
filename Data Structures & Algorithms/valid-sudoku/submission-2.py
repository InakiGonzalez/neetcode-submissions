from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        nums = set(["0","1","2","3","4","5","6","7","8","9"])
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                idx = (i // 3) * 3 + (j // 3)

                if num not in nums:
                    continue

                if num not in rows[i] and num not in cols[j] and num not in squares[idx]:
                    rows[i].append(num)
                    cols[j].append(num)
                    squares[idx].append(num)
                    
                else:
                    return False
        return True

