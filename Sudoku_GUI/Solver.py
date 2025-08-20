def solver(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for num in range(1,10):
                    if is_valid(board,i , j , num):
                        board[i][j]=num
                        if solver(board):
                            return True
                        

