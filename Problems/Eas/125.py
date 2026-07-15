# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
       s.strip()
       s = ''.join(c.lower() for c in s if c.isalnum())
       if s == s[::-1]:
           return True
       return False
           
my_solution = Solution()
print(my_solution.isPalindrome("A man, a plan, a canal: Panama")) # True
print(my_solution.isPalindrome("race a car")) # False
print(my_solution.isPalindrome(" ")) # True 