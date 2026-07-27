class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)
    
my_solution = Solution()
print(my_solution.maxProduct(nums = [3,4,5,2]))   #Output: 12
print(my_solution.maxProduct(nums = [1,5,4,5]))   #Output: 16