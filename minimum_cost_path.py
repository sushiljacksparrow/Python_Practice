class Solution:
    def minCostPath(self, cost) -> int:
        n = len(cost[0])
        m = len(cost)

        original = [[0 for i in range(m)] for j in range(n)]
        original[0][0] = cost[0][0]

        for i in range(1, n):
            original[i][0] = cost[i-1][0] + original[i][0]

        for j in range(1, m):
            original[0][j] = original[0][j] + cost[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                original[i][j] = cost[i][j] + \
                    min(original[i-1][j-1], original[i-1][j], original[i][j-1])

        return original[n-1][m-1]


if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    sol = Solution()
    print(sol.minCostPath(cost))
