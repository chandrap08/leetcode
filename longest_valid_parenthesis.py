class Solution(object):
    def longestValidParentheses(self, s):
        dp=[0]*(len(s)+1)
        for i in range(2,len(s)+1):
            if s[i-1]==')':
                dp[i]=dp[i-2]+2 if s[i-2]=='(' else (dp[i-1]+2+dp[i-2-dp[i-1]] if (i>=2+dp[i-1] and s[i-2-dp[i-1]]=='(') else 0)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("()()"))


