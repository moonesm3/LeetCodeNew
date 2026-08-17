#Classic Dp --> Be careful about the time complexity for Python. Probable to get TIL.
class Solution: 
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        #To not check everything on the way!
        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = right_best[i][i] = stoneValue[i]
        for length in range(2, n + 1):
            k = 0
            for i in range(n - length + 1):
                j = i + length - 1
                if k < i:
                    k = i
                while k < j and (prefix[k + 1] - prefix[i] <= prefix[j + 1] - prefix[k + 1]):
                    k += 1
                if k > i:
                    dp[i][j] = max(dp[i][j], left_best[i][k - 1])
                if k > i:
                    left_sum = prefix[k] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[k]
                    if left_sum == right_sum:
                        dp[i][j] = max(dp[i][j], right_best[k][j])
                if k < j:
                    dp[i][j] = max(dp[i][j], right_best[k + 1][j])
                total = prefix[j + 1] - prefix[i]
                left_best[i][j] = max(left_best[i][j - 1], total + dp[i][j])
                right_best[i][j] = max(right_best[i + 1][j], total + dp[i][j])

        return dp[0][n - 1]

my_solution = Solution()
print(my_solution.stoneGameV(stoneValue = [6,2,3,4,5,5]))     #Output: 18
print(my_solution.stoneGameV(stoneValue = [7,7,7,7,7,7,7]))     #Output: 28
print(my_solution.stoneGameV(stoneValue = [4]))     #Output: 0