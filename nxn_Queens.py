def Queens(n):
    result=[]
    def queen_check(array,n,cnt):
        if cnt==n:
          result.append(array) 
          cnt = 0 
        for row in range(n):
            for col in range(n):
                if array[row][col]=='':
                    is_Queen_Valid(row,col,array,n)
                    array[row][col]="Q"
                    queen_range(row,col,array,n)
                    cnt+=1
                    if queen_check(array,n,cnt):
                        return True
                    array[row][col]=''
    def is_Queen_Valid(row,col,array,n):
        for i in range(n):
            if array[row][i] !='' or array[i][col]!='':
                return False
        for j in range(n):
            for k in range(n):
                if (j-k == row - col) or (j+k == row + col):
                    if array[j][k]!="":
                        return False
        return True
    
    def queen_range(row,col,array,n):
         for i in range(n):
            if i != col:
                array[row][i] = "."
            if i != row:
                array[i][col] = "."
         for j in range(n):
            for k in range(n):
                if (j == row) and (k == col):
                    continue
                if (j-k == row - col) or (j+k == row + col):
                    array[j][k]="."

    grid = [["" for _ in range(n)] for _ in range(n)]
    queen_check(grid,n,0)
    return result
print(Queens(4))
                       
                       

                