def minCostClimbingStairs(cost):
    def helper(i,momo={}):
        if i in momo:
            return momo[i]
        if i >=len(cost):
            return 0
        momo[i]= cost[i]+min(helper(i+1,momo), helper(i+2,momo))
        return momo[i]
    return min(helper(0),helper(1))
    
print(minCostClimbingStairs([10, 15, 20]))

    