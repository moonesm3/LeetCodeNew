class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'   # A dummy character to avoid empty stack issues --> Don't delete this line, it is important for the code to work correctly

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
my_solution = Solution()
print(my_solution.isValid("()"))  # Output: True
print(my_solution.isValid("()[]{}"))  # Output: True
print(my_solution.isValid("(]"))  # Output: False
print(my_solution.isValid("([)]"))  # Output: False