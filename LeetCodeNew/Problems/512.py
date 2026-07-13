class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1        
        return max(len(a), len(b))
    
    
    
my_solution = Solution()
print(my_solution.findLUSlength(a = "aba", b = "cdc"))    #Output: 3
print(my_solution.findLUSlength(a = "aaa", b = "bbb"))    #Output: 3
print(my_solution.findLUSlength(a = "aaa", b = "aaa"))    #Output: -1