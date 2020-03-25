class Solution:
    def maxSumIncreasingSubSequence(self, arr) -> int:
        n = len(arr)
        dp = [0 for i in range(n)]
        for i in range(n):
            dp[i] = arr[i]

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[i] + dp[j]:
                    dp[i] = dp[i] + arr[j]
        return max(dp)


if __name__ == '__main__':
    arr = [1, 101, 2, 3, 100, 4, 5]
    sol = Solution()
    print(sol.maxSumIncreasingSubSequence(arr))
