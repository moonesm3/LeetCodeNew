class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
my_solution = Solution()
print(my_solution.strStr("sadbutsad","sad"))  # Output: 0
print(my_solution.strStr("leetcode","leeto"))  # Output: -1