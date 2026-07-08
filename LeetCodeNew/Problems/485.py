class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0
        return maximum
    
my_solution = Solution()
print(my_solution.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))   #Output: 3
print(my_solution.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))   #Output: 2    