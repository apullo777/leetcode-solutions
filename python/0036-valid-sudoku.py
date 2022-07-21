# https://leetcode.com/problems/valid-sudoku/

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(board):
            for row in board:
                if not isValid(row):
                    return False
            return True
        
        def isValidColumn(board):
            for column in zip(*board):
                if not isValid(column):
                    return False
            return True
        
        def isValidSquare(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i+3)
                                          for y in range(j, j+3)]
                    if not isValid(square):
                        return False
            return True
        
        def isValid(unit):
            unit = [i for i in unit if i != "."]
            return len(unit) == len(set(unit))
        
        return isValidRow(board) and isValidColumn(board) and isValidSquare(board)