class Solution:
    def maxProfit(self, k, prices) -> int:
        n = len(prices)
        mem = [[0 for i in range(k+1)] for j in range(n)]

        for i in range(1, n):
            for j in range(1, k+1):
                max_so_far = 0
                for l in range(i):
                    max_so_far = max(
                        max_so_far, prices[i] - prices[l] + mem[l][j-1])
                mem[i][j] = max(max_so_far, mem[i-1][j])
        return mem[n-1][k]


if __name__ == '__main__':
    prices = [10, 22, 5, 75, 65, 80]
    # [3, 2, 6, 5, 0, 3]
    k = 2
    sol = Solution()
    print(sol.maxProfit(k, prices))
