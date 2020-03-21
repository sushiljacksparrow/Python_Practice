class Solution:
    def minPathSum(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, m):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[n-1][m-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    sol = Solution()
    print(sol.minPathSum(grid))
