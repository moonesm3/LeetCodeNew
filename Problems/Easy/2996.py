class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        while total in nums:
            total += 1
        return total


my_solution = Solution()
print(my_solution.missingInteger(nums = [1,2,3,2,5]))    #Output: 6
print(my_solution.missingInteger(nums = [3,4,5,1,12,14,13]))    #Output: 15
