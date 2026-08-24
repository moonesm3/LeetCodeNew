class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        Alice = [0] * n
        Alice[0] = stones[0]

        for i in range(1, n):
            Alice[i] = Alice[i - 1] + stones[i]

        best = Alice[-1]
        for i in range(n - 2, 0, -1):
            best = max(best, Alice[i] - best)
        return best
    
my_solution = Solution()
print(my_solution.stoneGameVIII(stones = [-1,2,-3,4,-5]))     #Output: 5
print(my_solution.stoneGameVIII(stones = [7,-6,5,10,5,-2,-6]))     #Output: 13
print(my_solution.stoneGameVIII(stones = [-10,-12]))     #Output: -22

