class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0


my_solution = Solution()
nums = [0, 1, 0, 3, 12]
my_solution.moveZeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]