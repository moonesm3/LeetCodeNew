class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set(nums)
        disappeared = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                disappeared.append(i)
        return disappeared
        
        
my_solution = Solution()
print(my_solution.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(my_solution.findDisappearedNumbers(nums = [1,1]))