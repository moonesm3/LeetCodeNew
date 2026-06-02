# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in s:
            value = roman_numerals[char]
            if prev_value < value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        
        return total

my_solution = Solution()
print(my_solution.romanToInt("III")) # 3
print(my_solution.romanToInt("LVIII")) # 58