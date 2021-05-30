1. mine 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                box = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != ".":
                            if board[x][y] in box:
                                return False
                            box.add(board[x][y])
        return True                    
        
 2. answer use function, more readable
 def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True
    
def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)
