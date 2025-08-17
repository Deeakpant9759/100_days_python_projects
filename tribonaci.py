def tribonacci(n: int) -> int:
    def helper(i,momo=None):
        if momo is None:
            momo = {0:0, 1:1, 2:1}
        if i in momo:
            return momo[i]
        momo[i] = helper(i-1,momo)+helper(i-2,momo)+helper(i-3,momo)
        return momo[i]
    return helper(n)
print(tribonacci(4))
