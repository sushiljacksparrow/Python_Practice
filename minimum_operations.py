# https://practice.geeksforgeeks.org/problems/find-optimum-operation/0
def minimum_operations(n) -> int:
    dp = [float('Inf')]*(n+1)
    dp[0], dp[1], dp[2] = 0, 1, 2

    for i in range(3, n+1):
        dp[i] = min(dp[i], dp[i-1] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[int(i/2)] + 1)

    return dp[n]


if __name__ == '__main__':
    t = input()
    for i in range(int(t)):
        n = input()
        print(minimum_operations(int(n)))
