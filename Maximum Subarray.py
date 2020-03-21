class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        max_so_far = 0
        max_ending_here = 0
        for i in range(n):
            max_ending_here = max_ending_here + nums[i]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return max_so_far


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums))
