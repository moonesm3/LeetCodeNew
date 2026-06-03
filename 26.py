# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    
my_solution = Solution()
print(my_solution.removeDuplicates([1,1,2]))  # Output: 2
print(my_solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5