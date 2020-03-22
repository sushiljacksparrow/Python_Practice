class Solution:
    def minimumPartition(self, s) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        palindrome = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            palindrome[i][i] = True
            dp[i][i] = 0

        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i+L-1
                if L == 2:
                    palindrome[i][j] = (s[i] == s[j])
                else:
                    palindrome[i][j] = (
                        (s[i] == s[j]) and palindrome[i+1][j-1])

                if palindrome[i][j] is True:
                    dp[i][j] = 0
                else:
                    dp[i][j] = float('Inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)
        return dp[0][n-1]


if __name__ == '__main__':
    s = 'ababbbabbababa'
    sol = Solution()
    print(sol.minimumPartition(s))
