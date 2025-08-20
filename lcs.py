def longestCommonSubsequence(text1, text2):
    #write code here
    result=[]
    def backtract(i,current):
        if text2 ==current:
            return len(text2)
        if i == len(text1):
            result.append(current[:])
            return
        current.append(text1[i])
        backtract(i+1,current)
        current.pop()
        backtract(i+1,current)
        return 0
    return backtract(0,[])
    