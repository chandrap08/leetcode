class Solution(object):
    def swimInWater(grid):
        N = len(grid)
        lo = grid[0][0]
        hi = N * N - 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # dfs
        def valid(val):
            visited = [[False] * N for _ in range(N)]
            onpath = {(0, 0)}
            while onpath:
                i, j = onpath.pop()
                visited[i][j] = True
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if 0 <= x < N and 0 <= y < N and not visited[x][y] and grid[x][y] <= val:
                        if x == y == N - 1: return True
                        onpath.add((x, y))
            return False
            # Binary search

        while lo < hi:
            mi = (lo + hi) // 2
            if valid(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


