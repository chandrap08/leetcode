class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        if s == "" or t == "": return 0
        if s == t: return 1
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1

        for i in range(m+1):
            for j in range(n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[m][n]

if __name__ == "__main__":
    S = "ccc"
    T = "c"
    print(Solution().numDistinct(S,T))
