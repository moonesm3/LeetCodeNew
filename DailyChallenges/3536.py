class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort(reverse=True)
        return digits[0] * digits[1]
    

my_solution = Solution()
print(my_solution.maxProduct(n = 31))     #Output: 3