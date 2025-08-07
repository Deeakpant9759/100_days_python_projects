def sudoki_solver(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_valid(board,i,j,num):
                        board[i][j] = num
                        if sudoki_solver(board):
                            return True
                        board[i][j] = 0
                return False
    return True
            
def is_valid(board,row,col,num):
    for i in range(9):
        if board[row][i] ==num or board[i][col]==num:
            return False
    start_row , start_col = 3*(row//3),3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j]==num:
                return False
    return True    

test_board = [
    [5, 3, 0, 6, 7, 0, 9, 0, 0],   # Row 0
    [6, 7, 0, 1, 9, 5, 0, 0, 8],   # Row 1
    [0, 9, 8, 0, 0, 0, 0, 6, 0],   # Row 2  ← (2,3) is 0 → We'll test here
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],   # Row 5  ← (5,6) will be problematic
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoki_solver(test_board)   
print(test_board)