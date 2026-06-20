class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # worst case scenario is O(81)
        # we should check every  cell that has a number, if it has . then we skip it
        # we should check three locations: samw row, same col and same 3x3 square 
        # we can use sets for rwos, cols and squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                print("r: ",r)
                print("c: ",c)
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3 , c // 3)].add(board[r][c])
        return True