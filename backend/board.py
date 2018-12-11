

class Board:
    def __init__(self, n=5, m=5,):
        # rows
        self.m = m

        # columns
        self.n = n

        self.board = [[0 for x in range(n)] for y in range(m)]

    def __str__(self,):
        return str(self.board)

    def add_wall_borders(self,):
        for idx_row, row in enumerate(self.board):
            for idx_col, col in enumerate(row):
                if idx_row == 0 or idx_row == self.m - 1:
                    self.board[idx_row][idx_col] = 1
                elif idx_col == 0 or idx_col == self.n - 1:
                    self.board[idx_row][idx_col] = 1
