class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for sticks in range(1, n + 1):
            for visible in range(min(sticks, k), 0, -1):
                dp[visible] = (dp[visible - 1] + (sticks - 1) * dp[visible]) % MOD
            dp[0] = 0
        return dp[k]
    

my_solution = Solution()
print(my_solution.rearrangeSticks(n = 3, k = 2))   #Output: 3
print(my_solution.rearrangeSticks(n = 5, k = 5))   #Output: 1
print(my_solution.rearrangeSticks(n = 20, k = 11))   #Output: 647427950