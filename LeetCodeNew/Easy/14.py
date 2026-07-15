# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
    
my_solution = Solution()
print(my_solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"