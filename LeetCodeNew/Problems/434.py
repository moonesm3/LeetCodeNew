class Solution:
    def countSegments(self, s: str) -> int:
        string = s.split()
        return len(string)
        
        
my_solution = Solution()
print(my_solution.countSegments(s = "Hello, my name is John"))
print(my_solution.countSegments(s = ""))