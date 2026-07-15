class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

my_solution = Solution()
print(my_solution.missingNumber([3, 0, 1]))  # 2
print(my_solution.missingNumber([9,6,4,2,3,5,7,0,1]))  # 8