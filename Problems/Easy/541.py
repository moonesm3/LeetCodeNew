class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i:i + k] = reversed(chars[i:i + k])
        return "".join(chars)
    
my_solution = Solution()
print(my_solution.reverseStr(s = "abcdefg", k = 2))     #Output: "bacdfeg"
print(my_solution.reverseStr(s = "abcd", k = 2))     #Output: "bacd"