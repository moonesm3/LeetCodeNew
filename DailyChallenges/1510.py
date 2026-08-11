class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for stones in range(1, n + 1):
            square = 1
            while square * square <= stones:
                remaining = stones - square * square
                if dp[remaining] == False:
                    dp[stones] = True
                    break
                square += 1
        return dp[n]


my_solution = Solution()
print(my_solution.winnerSquareGame(n = 1))    #Output: True
print(my_solution.winnerSquareGame(n = 2))    #Output: False
print(my_solution.winnerSquareGame(n = 4))    #Output: True
