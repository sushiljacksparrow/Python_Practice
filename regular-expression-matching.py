class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        # when both s and p are 0 length
        mem[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                mem[0][j] = mem[0][j-1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    mem[i][j] = mem[i][j-1] or mem[i-1][j]
                elif p[j-1] == '.' or s[i-1] == p[j-1]:
                    mem[i][j] = mem[i-1][j-1]
                else:
                    mem[i][j] = False

        return mem[len(s)][len(p)]


if __name__ == '__main__':
    sol = Solution()
    s = 'aab'
    p = '*a*b'
    print(sol.isMatch(s, p))
