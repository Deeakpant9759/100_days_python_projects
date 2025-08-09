def Queens(n):
    result=[]
    def queen_check(board,n,row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_Queen_Valid(row,col,board,n):
                board[row][col] = 'Q'
                queen_check(board,n,row+1)
                board[row][col]='.'

    def is_Queen_Valid(row,col,baord,n):
        for i in range(n):
            if baord[row][i] =='Q' or baord[i][col]=='Q':
                return False
        for j in range(n):
            for k in range(n):
                if (j-k == row - col) or (j+k == row + col):
                    if baord[j][k]=='Q':
                        return False
        return True
    board = [['.' for _ in range(n)] for _ in range(n)]
    queen_check(board,n,0)
    return len(result)

print(Queens(8))
                       
                       

                