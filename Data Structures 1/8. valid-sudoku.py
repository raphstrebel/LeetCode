class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        col = set()
        for i in range(n):
            line = set()
            square = set()
            for j in range(n):
                if board[i][j] in line and board[i][j] != '.':
                    return False
                line = line.union({board[i][j]})
                if board[j][i] in col and board[j][i] != '.':
                    return False
                col = col.union({board[j][i]})
                square_i, square_j = divmod(i*9+j, 3)
                if 9 <= square_i and square_i < 18:
                    square_i = square_i%9
                    square_j += 3
                if 18 <= square_i and square_i < 27:
                    square_i = square_i%9
                    square_j += 6
                if board[square_i][square_j] in square and board[square_i][square_j] != '.':
                    return False
                square = square.union({board[square_i][square_j]})
            col = set()
        return True