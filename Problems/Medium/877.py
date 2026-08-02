#Check 486.py problem --> the same solution
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                take_left = piles[left] - dp[left + 1][right]
                take_right = piles[right] - dp[left][right - 1]
                dp[left][right] = max(take_left, take_right)
        return dp[0][n - 1] >= 0    #if positive --> 1 wins!
 
my_solution = Solution()
print(my_solution.stoneGame(piles = [5,3,4,5]))    #Ouput: True
print(my_solution.stoneGame(piles = [3,7,2,3]))    #Ouput: True