# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
def maximum_size_submatrix(m) -> int:
    rows = len(m)
    cols = len(m[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]

    # copy the first column
    for i in range(rows):
        dp[i][0] = m[i][0]
    # copy the first row
    for j in range(cols):
        dp[0][j] = m[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            if m[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    max_len = 0
    row_index = 0
    col_index = 0

    for i in range(rows):
        for j in range(cols):
            if dp[i][j] >= max_len:
                max_len = dp[i][j]
                row_index = i
                col_index = j
    return max_len, row_index, col_index


if __name__ == '__main__':
    m = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    print(maximum_size_submatrix(m))
