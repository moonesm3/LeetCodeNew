class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            current_sum = 0
            dp[i] = float("-inf")
            for take in range(1, 4):
                if i + take > n:
                    break
                current_sum += stoneValue[i + take - 1]
                dp[i] = max(dp[i], current_sum - dp[i + take])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        
my_solution = Solution()
print(my_solution.stoneGameIII(stoneValue = [1,2,3,7]))    #Output: "Bob"
print(my_solution.stoneGameIII(stoneValue = [1,2,3,-9]))    #Output: "Alice"
print(my_solution.stoneGameIII(stoneValue = [1,2,3,6]))    #Output: "Tie"