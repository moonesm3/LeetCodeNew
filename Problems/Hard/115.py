#Be careful about TLE
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char in s:
            for j in range(len(t) - 1, -1, -1):
                if char == t[j]:
                    dp[j + 1] += dp[j]
        return dp[len(t)]


my_solution = Solution()
print(my_solution.numDistinct(s = "rabbbit", t = "rabbit"))    #Output: 3
print(my_solution.numDistinct(s = "babgbag", t = "bag"))    #Output: 5