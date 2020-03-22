class Solution:
    def longestIncreaseSubsequence(self, arr: list) -> list:
        n = len(arr)
        mem = [1 for i in range(n)]

        reconstruct = [-1 for i in range(n)]
        for i in range(n):
            reconstruct[i] = i

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    mem[i] = max(mem[i], mem[j] + 1)
                    reconstruct[i] = j
        print(reconstruct)
        return mem


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    sol = Solution()
    print(sol.longestIncreaseSubsequence(arr))
