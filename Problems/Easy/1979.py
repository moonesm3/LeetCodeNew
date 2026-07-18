from math import gcd
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        return gcd(minimum, maximum)
        
my_solution = Solution()
print(my_solution.findGCD(nums = [2,5,6,9,10]))     #Output: 3
print(my_solution.findGCD(nums = [7,5,6,8,3]))     #Output: 1