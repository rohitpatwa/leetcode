# Create 2 arrays rows and cols of size n. For each move +1 or or -1 the respective row and cols. For diagonals just store 2 variables d1 and d2.

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0]*n
        self.cols = [0]*n
        self.d1 = 0
        self.d2 = 0
        self.p = [None, 1, -1]
        self.winning_number = n
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        n = len(self.rows)
        
        self.rows[row] += self.p[player]
        if abs(self.rows[row]) == self.winning_number:
            return player
        
        self.cols[col] += self.p[player]
        if abs(self.cols[col]) == self.winning_number:
            return player
        
        if row==col:
            self.d1 += self.p[player]
            if abs(self.d1) == self.winning_number:
                return player
        
        if row+col==n-1:
            self.d2 += self.p[player]
            if abs(self.d2) == self.winning_number:
                return player
        
        return 0
