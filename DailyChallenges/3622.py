class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        digit_sum = 0
        digit_product = 1
        while x > 0:
            digit = x % 10
            digit_sum += digit
            digit_product *= digit
            x //= 10
        return n % (digit_sum + digit_product) == 0

my_solution = Solution()
print(my_solution.checkDivisibility(n = 99))   #Output: True
print(my_solution.checkDivisibility(n = 23))   #Output: Falsex