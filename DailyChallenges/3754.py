class Solution:
    def sumAndMultiply(self, n: int) -> int:
        m = 0
        count = 1
        digit_sum = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                m += count * digit
                digit_sum += digit
                count *= 10
            n = n // 10
        return m * digit_sum    
        
        
my_solution = Solution()
print(my_solution.sumAndMultiply(n = 120))
print(my_solution.sumAndMultiply(n = 10203004))
                