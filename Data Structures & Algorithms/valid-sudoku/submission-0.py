class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            freq = [0]*10
            for block in row:
                if block != '.':
                    if freq[int(block)] == 1:
                        return False
                    else:
                        freq[int(block)] += 1
                

        # check cols
        for col in zip(*board):
            freq = [0]*10
            for block in col:
                if block != '.':
                    if freq[int(block)] == 1:
                        return False
                    else:
                        freq[int(block)] += 1

        # check 3x3
        for i in range(0,3):
            for j in range(0,3):
                freq = [0] * 10
                for k in range(0,3):
                    for l in range(0,3):
                        if board[3*i+k][3*j+l] != '.':
                            if freq[int(board[3*i+k][3*j+l])] == 1:
                                return False
                            else:
                                freq[int(board[3*i+k][3*j+l])] += 1
        
        return True


        