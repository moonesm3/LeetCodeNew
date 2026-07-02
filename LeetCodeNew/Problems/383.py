class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, "", 1)
        return True
    
my_solution = Solution()
print(my_solution.canConstruct(ransomNote = "a", magazine = "b"))    #Output: False
print(my_solution.canConstruct(ransomNote = "aaa", magazine = "baaa"))    #Output: True
print(my_solution.canConstruct(ransomNote = "a", magazine = "ab"))    #Output: True