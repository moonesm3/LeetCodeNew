class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        m = s + s
        m = m[1:-1]
        if s in m:
            return True 
        return False
            
            
        
        

my_solution = Solution()
print(my_solution.repeatedSubstringPattern(s = "abab"))
print(my_solution.repeatedSubstringPattern(s = "aba"))
print(my_solution.repeatedSubstringPattern(s = "abcabcabcabc"))
print(my_solution.repeatedSubstringPattern(s = "bb"))
