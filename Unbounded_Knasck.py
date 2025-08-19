def knapSack(W, wt, val, n):
    def helper(i,rm,memo=None):
        if memo is None:
            memo = [[-1]*(W+1)for _ in range(n+1)]
        if memo[i][rm] != -1:
            return memo[i][rm]
        if i == 0 or rm == 0:
            return 0
        exclude = helper(i-1,rm,memo)
        include = 0
        if wt[i-1] <= rm:
            include = val[i-1] + helper(i,rm-wt[i-1],memo)
        memo[i][rm] = max(include, exclude)
        return memo[i][rm]
    return helper(n,W)
print(knapSack(4, [3,1], [2,2], 2))  # Output: 8