# Scan through each word in grid. Where 1st char matches, perform dfs on it's neighbors. Replace a visited word by -1 to avoid visiting it again. Backtrack if needed.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.m, self.n = len(board), len(board[0])
        
        # Go through each element of the array
        # If the first char matches with the word, call helper function
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.helper(board, i, j, 0, word):
                    return True
        return False
    
    def helper(self, board, i, j, idx, word):
        
        # Here idx value signifies that chars upto idx have been matched
        # If below cond. is true, this means whole word has been found,
        # so return True
        if idx==len(word)-1:
            return True
        
        # Update the board char with -1 so that you do not revisit this char in
        # this iteration
        board[i][j], original_char = -1, board[i][j]
        
        # Visit the 4 neighbors of the (i,j)th position
        for (a,b) in [[i-1, j], [i,j+1], [i+1,j], [i,j-1]]:
            # Check if the neighbor is at a valid index
            if a>=0 and a<self.m and b>=0 and b<self.n:
                # Check if the neighbor matches the next char of word
                # If yes, call helper again with neighbor's position and idx+1
                if board[a][b] == word[idx+1] and self.helper(board, a, b, idx+1, word):
                    return True
        
        # If none of the neighbors returned True, backtrack and reset the original value
        # of that position on the board.
        board[i][j] = original_char
        
        return False