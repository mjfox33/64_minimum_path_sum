class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) # assuming every row has the same number of columns
        dp = [ [0]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for row in range(n):
            for col in range(m):
                dp[row][col] = grid[row][col]
                if row == 0 and col > 0:
                    dp[row][col] += dp[row][col-1]
                elif row > 0 and col == 0:
                    dp[row][col] += dp[row-1][col]
                else:
                    dp[row][col] += min(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]