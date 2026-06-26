import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        m = math.sqrt(num)
        n = int(m)
        if (n * n == num):
            return True
        return False
    
my_solution = Solution()
print(my_solution.isPerfectSquare(16))
print(my_solution.isPerfectSquare(14))