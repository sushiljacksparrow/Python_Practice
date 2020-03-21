class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        # represents first i charecters of w1 and j of w2
        mem = [[0 for i in range(l1+1)] for j in range(l2+1)]

        for i in range(l1+1):
            mem[i][0] = i
        for j in range(l2+1):
            mem[0][j] = j

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] is not word2[j-1]:
                    mem[i][j] = min(mem[i-1][j], mem[i]
                                    [j-1], mem[i-1][j-1]) + 1
                else:
                    mem[i][j] = mem[i-1][j-1]

        return mem[l1][l2]


if __name__ == '__main__':
    word1 = 'intention'
    word2 = 'execution'
    sol = Solution()
    print(sol.minDistance(word1, word2))
