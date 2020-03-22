class Solution:
    def multiplication(self, arr) -> int:
        n = len(arr)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n):
            dp[i][i] = 0

        for l in range(2, n):
            for i in range(1, n-l+1):
                j = i + l - 1
                dp[i][j] = float('Inf')
                for k in range(i, j):
                    q = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    if q < dp[i][j]:
                        dp[i][j] = q
        return dp[1][n-1]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    sol = Solution()
    print(sol.multiplication(arr))
