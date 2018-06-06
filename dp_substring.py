# Find the least common string

def lcs(x,y):
    l1 = len(x)
    l2 = len(y)

    dp = [[0] * (l1+1) for i in range(l2 + 1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 and j ==0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[l1][l2]

X = 'AGGTAB'
Y = "GXTXAYB"
lcs(X,Y)

