def longestCommonSubsequence(text1, text2):
    #write code here
    n = len(text1)
    m = len(text2)
    def helper(index1,index2):
        if index1 >=n-1 or index2 >= m-1:
            return 0
        if text1[index1] == text2[index2]:
            return 1+helper(index1+1, index2+1)
        return max(helper(index1+1, index2), helper(index1, index2+1))

    return helper(0, 0)

print(longestCommonSubsequence("ezupkr", "ubmrapg"))  # Output: 3