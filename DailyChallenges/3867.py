from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        current_max = 0
        for number in nums:
            current_max = max(current_max, number)
            prefix_gcd.append(gcd(number, current_max))

        prefix_gcd.sort()
        total = 0
        left = 0
        right = len(prefix_gcd) - 1
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        return total
    

my_solution = Solution()
print(my_solution.gcdSum(nums = [2,6,4]))       #Output: 2
print(my_solution.gcdSum(nums = [3,6,2,8]))       #Output: 5