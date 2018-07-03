class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        dp = [[[None] * N for _1 in range(N)] for _2 in range(N)]

        for d in dp:
            print(d)


if __name__ == "__main__":
    s = Solution()
    grid = [[0, 1, -1],
            [1, 0, -1],
            [1, 1,  1]]
    s.cherryPickup(grid)