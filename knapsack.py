def knapsack(weights, values, w) -> int:
    n = len(weights)
    dp = [0]*(w+1)

    for i in range(1, w+1):
        for j in range(n):
            if i - weights[j] >= 0:
                dp[i] = max(dp[i-1], dp[i-weights[j]] + values[j])

    return dp[w]


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    print(knapsack(weights, values, 50))
