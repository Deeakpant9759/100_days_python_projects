def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0:
        return cost[0]
    if n == 1:
        return cost[1]
    