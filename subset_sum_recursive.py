class Solution:
    def subsetSum(self, arr, sum, n) -> bool:
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False

        if arr[n-1] > sum:
            return self.subsetSum(arr, n-1, sum)

        return self.subsetSum(arr, sum - arr[n-1], n-1) or self.subsetSum(arr, sum, n-1)


if __name__ == '__main__':
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    sol = Solution()
    print(sol.subsetSum(arr, sum, len(arr)))
