# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            return str(x) == str(x)[::-1]
        return False    
    
my_solution = Solution()
print(my_solution.isPalindrome(121)) # True
print(my_solution.isPalindrome(123)) # False