class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        total_sum = sum(nums)
        target = total_sum // 2
        def backtrack(i,current_sum):
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]
            if current_sum == target:
                return True
            if i == len(nums) or current_sum > target:
                return False
            if backtrack(i+1,current_sum + nums[i]):
                memo[(i,current_sum)] = True
                return True
            if backtrack(i+1,current_sum):
                memo[(i,current_sum)] = True
                return True
            memo[(i,current_sum)] = False
            return False
        return backtrack(0,0)  