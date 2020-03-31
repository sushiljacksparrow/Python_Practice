def minimal_moves(s) -> int:
    n = len(s)
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i % 2 == 1:
            dp[i] = dp[i-1] + 1
        else:
            k = int(i/2)
            flag = True
            for j in range(1, k+1):
                if s[j-1] is not s[k+j-1]:
                    flag = False
                    break
            if flag:
                dp[i] = dp[k] + 1
            else:
                dp[i] = dp[i-1] + 1
    return dp[n]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(minimal_moves(s))
