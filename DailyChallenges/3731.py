class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        nums.sort()
        y = nums[0]
        z = nums[-1]
        l = []
        for i in range(y,z,1):
            if i not in nums:
                l.append(i)
        return l
    
my_solution = Solution()
print(my_solution.findMissingElements(nums = [1,4,2,5]))   #Output:[3]
print(my_solution.findMissingElements(nums = [7,8,6,9]))   #Output:[]
       