class Solution:
    def canWinNim(self, n: int) -> bool:
            return n % 4 != 0
        
        
        
my_solution = Solution()
print(my_solution.canWinNim(4))
print(my_solution.canWinNim(1))