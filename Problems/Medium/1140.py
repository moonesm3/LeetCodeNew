#LeetCode, if you hear me my dear. Please stop with this Alice and Bob...
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        #Even you can check 3302.py
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        best_score = {}
        def dfs(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix[i]
            if (i, M) in best_score:
                return best_score[(i, M)]

            best = 0
            for X in range(1, 2 * M + 1):
                Bob = dfs(i + X, max(M, X))
                current = suffix[i] - Bob
                best = max(best, current)
            best_score[(i, M)] = best
            return best
        
        return dfs(0, 1)


my_solution = Solution()
print(my_solution.stoneGameII(piles = [2,7,9,4,4]))     #Output: 10
print(my_solution.stoneGameII(piles = [1,2,3,4,5,100]))     #Output: 104