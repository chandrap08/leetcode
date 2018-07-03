class Solution(object):
    def lcs(self,X,Y):
        m,n = len(X),len(Y)
        dp = [[None]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of LCS is ", Solution().lcs(X, Y))


