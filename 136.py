# 136. Single Number
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num
my_solution = Solution()
print(my_solution.singleNumber([2, 2, 1]))  # Output: 1
print(my_solution.singleNumber([4, 1, 2, 1, 2]))  # Output: 4