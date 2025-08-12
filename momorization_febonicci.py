def fabonacci(n,ht={0:0,1:1}):
    if n in ht :
        return ht[n]
    else:
        ht[n] = fabonacci(n-1)+fabonacci(n-2)
        return ht[n]
print(fabonacci(1000))