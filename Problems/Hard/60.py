from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        result = ""
        k -= 1
        while nums:
            block = factorial(len(nums) - 1)
            index = k // block
            result += nums.pop(index)
            k %= block
        return result
    
my_solution = Solution()
print(my_solution.getPermutation(n = 3, k = 3))   #Output: 213
print(my_solution.getPermutation(n = 4, k = 9))   #Output: 2314
print(my_solution.getPermutation(n = 3, k = 1))   #Output: 123