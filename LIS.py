def sequence(nums):
    n = len(nums)
    result =[]
    def helper(i,Prv):
        if i >n-1:
            return 0
        exclude = helper(i+1,Prv)
        include = 0
        if Prv == -1 or nums[i]>nums[Prv]:
            include = 1 + helper(i+1,i)
        return max(exclude,include)
    return helper(0,-1)
x = sequence([4,10,4,3,8,9])
print(x)
