class Solution:
    def numTilings(self, n: int) -> int:
        if n==1: return 1
        dp=[[0,0] for i in range(n+1)]
        dp[1]=[1,2]
        dp[2]=[2,4]
        for i in range(3,n+1):
            dp[i][0]=dp[i-1][0]+dp[i-2][0]+dp[i-2][1]
            dp[i][1]=dp[i-1][1]+2*dp[i-1][0]
        return dp[n][0]%1_000_000_007