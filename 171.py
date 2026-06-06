class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

my_solution = Solution()
print(my_solution.titleToNumber("A")) #Output: 1
print(my_solution.titleToNumber("ZY")) #Output: 701