class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]

        for c in range(1,col):
            dp[0][c] += dp[0][c - 1] + grid[0][c]

        for r in range(1,row):
            dp[r][0] += dp[r-1][0] + grid[r][0]

        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]

        print(dp)
        return dp[row-1][col-1]

if __name__ == "__main__":
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(Solution().minPathSum(grid))
