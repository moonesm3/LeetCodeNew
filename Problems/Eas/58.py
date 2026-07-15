# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        #print(f"Words: {words}")
        if words[-1] == '':
            return len(words[-2])
        return len(words[-1])
    
my_solution = Solution()
print(my_solution.lengthOfLastWord("Hello World"))  # Output: 5
print(my_solution.lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
print(my_solution.lengthOfLastWord("luffy is still joyboy")) # Output: 6