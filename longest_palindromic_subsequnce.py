# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
def longest_palindromic_subsequence(text: str) -> int:
    n = len(text)
    dp = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if text[i] == text[i+1]:
            dp[i][i+1] = 2

    for L in range(3, n+1):
        for i in range(n - L + 1):
            j = i + L - 1
            if text[i] == text[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    for i in range(n):
        print(dp[i])

    return dp[0][n-1]


if __name__ == '__main__':
    text = 'GEEKS FOR GEEKS'
    print(longest_palindromic_subsequence(text))
