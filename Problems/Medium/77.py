class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        combination = []
        def backtrack(start):
            if len(combination) == k:
                result.append(combination.copy())
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1)
                combination.pop()
        backtrack(1)
        return result
    
my_solution = Solution()
print(my_solution.combine(n = 4, k = 2))   #Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]