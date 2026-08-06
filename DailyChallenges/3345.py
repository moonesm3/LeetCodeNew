class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
         for i in range(n, n + 10):
            product = 1
            for digit in str(i):
                product *= int(digit)
            if product % t == 0:
                return i
            
my_solution = Solution()
print(my_solution.smallestNumber(n = 10, t = 2))     #Output: 10
print(my_solution.smallestNumber(n = 21, t = 2))     #Output: 21