class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        m = nums[-1] * nums[-2] * nums[-3]
        n = nums[0] * nums[1] * nums[-1]
        return max(m, n)
    
my_solution = Solution()
print(my_solution.maximumProduct(nums = [-1,-2,-3]))    #Output: -6