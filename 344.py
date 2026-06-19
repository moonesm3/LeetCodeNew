class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s
    
my_solution = Solution()
print(my_solution.reverseString(s = ["h","e","l","l","o"]))