class Solution:
    def longestCommonSubsequence(self, first: str, second: str) -> str:
        n = len(first)
        m = len(second)
        mat = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n):
            for j in range(m):
                if first[i] == second[j]:
                    mat[i+1][j+1] = mat[i][j] + 1
                else:
                    mat[i+1][j+1] = max(mat[i+1][j], mat[i][j+1])

        # code to create LCS
        index = mat[n][m]
        lcs = ['']*(index+1)
        i = n
        j = m
        while i > 0 and j > 0:
            if first[i-1] == second[j-1]:
                lcs[index-1] = first[i-1]
                i = i - 1
                j = j - 1
                index = index - 1
            elif mat[i-1][j] > mat[i][j-1]:
                i = i - 1
            else:
                j = j-1
        return ''.join(lcs)


if __name__ == '__main__':
    first = 'AGGTAB'
    second = 'GXTXAYB'
    sol = Solution()
    print(sol.longestCommonSubsequence(first, second))
