class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n >= 1):
            if (1162261467 % n == 0): 
                return True
        return False

my_solution = Solution()
print(my_solution.isPowerOfThree(9))
print(my_solution.isPowerOfThree(-1))
print(my_solution.isPowerOfThree(0))