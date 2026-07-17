def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

class Solution:  
    def trailingZeroes(self, n: int) -> int:
        fact = Factorial(n)
        count = 0
        while fact % 10 == 0:
            count += 1
            fact //= 10
        return count

my_solution = Solution()
print(my_solution.trailingZeroes(n = 3))   #Output: 0
print(my_solution.trailingZeroes(n = 5))   #Output: 1