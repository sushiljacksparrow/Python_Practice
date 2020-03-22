class Solution:
    def coinChange(self, n, coins) -> int:
        mem = [0]*(n+1)
        mem[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], n+1):
                mem[j] = mem[j] + mem[j-coins[i]]
        return mem[n]


if __name__ == '__main__':
    coins = [1, 2, 3]
    sol = Solution()
    print(sol.coinChange(4, coins))
