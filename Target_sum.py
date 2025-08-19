def canPartition(nums):
    result = []
    def backtract(i,current):
        if nums == current:
            return
        if i == len(nums):
            result.append(current[:])
            return 
        current.append(nums[i])
        backtract(i+1,current)
        current.pop()
        backtract(i+1,current)
    backtract(0,[])
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if sum(result[i])==sum(result[j]):
                return True
    return False
        
    