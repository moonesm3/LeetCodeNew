# 27. Remove Element
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
        y = 0
        for i in range(len(nums)):
            if nums[i] != '_':
                nums[y] = nums[i]
                y += 1
        return y
    
my_solution = Solution()
print(my_solution.removeElement([3,2,2,3], 3))  # Output: 2