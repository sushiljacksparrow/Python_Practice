class Solution:
    def maxLenPairChain(self, arr) -> int:
        arr = sorted(arr, key=lambda x: x[0])
        n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if arr[i][0] > arr[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        print(dp)
        return max(dp)


if __name__ == '__main__':
    arr = [[5, 24], [15, 25], [50, 60], [27, 40], [1, 5]]
    sol = Solution()
    print(sol.maxLenPairChain(arr))
