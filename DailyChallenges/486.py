#Read about Bob and Alice with the stone game --> easily done with the dynamic programming
class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                take_left = nums[left] - dp[left + 1][right]
                take_right = nums[right] - dp[left][right - 1]
                dp[left][right] = max(take_left, take_right)
        return dp[0][n - 1] >= 0    #if positive --> 1 wins!
    

my_solution = Solution()
print(my_solution.predictTheWinner(nums = [1,5,2]))    #Output: False
print(my_solution.predictTheWinner(nums = [1,5,233,7]))    #Output: True