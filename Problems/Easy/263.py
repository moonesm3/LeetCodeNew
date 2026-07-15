class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0:
            if n == 1:
                return True
            elif n % 2 == 0:
                return self.isUgly(n // 2)
            elif n % 3 == 0:
                return self.isUgly(n // 3)
            elif n % 5 == 0:
                return self.isUgly(n // 5)
            else:
                return False

        return False
    
my_solution = Solution()
print(my_solution.isUgly(1))    #Output: True
print(my_solution.isUgly(17)) #Output: False