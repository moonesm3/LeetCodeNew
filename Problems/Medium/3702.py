class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        if total_xor != 0:
            return len(nums)
        for num in nums:
            if num != 0:
                return len(nums) - 1
        return 0

my_solution = Solution()
print(my_solution.longestSubsequence(nums = [1,2,3]))    #Output: 2
print(my_solution.longestSubsequence(nums = [2,3,4]))    #Output: 3