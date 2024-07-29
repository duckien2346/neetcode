from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if (
                    value in row[r] or
                    value in col[c] or
                    value in square[(r//3,c//3)]
                ):
                    return False
                row[r].add(value)
                col[c].add(value)
                square[(r//3,c//3)].add(value)
        return True

board = [
["1","2",".", ".","3",".", ".",".","."],
["4",".",".", "5",".",".", ".",".","."],
[".","9","8", ".",".",".", ".",".","3"],

["5",".",".", ".","6",".", ".",".","4"],
[".",".",".", "8",".","3", ".",".","5"],
["7",".",".", ".","2",".", ".",".","6"],

[".",".",".", ".",".",".", "2",".","."],
[".",".",".", "4","1","9", ".",".","8"],
[".",".",".", ".","8",".", ".","7","9"]
]
resolve = Solution()
result = resolve.isValidSudoku(board)
print(result)
