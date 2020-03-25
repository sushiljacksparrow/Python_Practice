class Solution:
    def minimumJumps(self, arr) -> int:
        n = len(arr)
        dp = [float('Inf') for _ in range(n)]

        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if (j + arr[j]) >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        print(dp)
        return dp[n-1]


if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    sol = Solution()
    print(sol.minimumJumps(arr))
