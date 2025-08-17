def mincost(cost):
    n = len(cost)
    for i in range(n+1,0,-1):
        total = min(cost[i-1], cost[i-2]) + cost[i]
    return total
print(mincost([10, 15, 20]))