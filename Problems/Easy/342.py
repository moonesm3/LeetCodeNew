import math

def logn(n, base):
    return math.log(n) / math.log(base)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        logarithm = logn(n, 4)
        return math.floor(logarithm) == math.ceil(logarithm)
    

my_solution = Solution()
print(my_solution.isPowerOfFour(1))
print(my_solution.isPowerOfFour(4))
print(my_solution.isPowerOfFour(10))
