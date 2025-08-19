def knapSack(W, wt, val, n):
    def helper(i , rem_wt,memo=None):
        if memo is None:
            memo = [[-1]*(W+1) for _ in range(n)]
        if memo[i][rem_wt] != -1:
            return memo[i][rem_wt] 
        if i >=n or rem_wt == 0:
            return 0
        exclude = helper(i+1,rem_wt,memo)
        include = 0
        if wt[i]<=rem_wt:
            include = val[i] + helper(i+1,rem_wt-wt[i],memo)
        memo[i][rem_wt] = max(exclude,include)
        return memo[i][rem_wt]
    return helper(0,W)  