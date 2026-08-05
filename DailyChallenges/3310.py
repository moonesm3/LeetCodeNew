class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        suspicious = set()
        def dfs(method):
            if method in suspicious:
                return
            suspicious.add(method)
            for next_method in graph[method]:
                dfs(next_method)
        dfs(k)
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        return [method for method in range(n) if method not in suspicious]
    
my_solution = Solution()
print(my_solution.remainingMethods(n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]))   #Output: [0,1,2,3]
print(my_solution.remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]))   #Output: [3,4]
print(my_solution.remainingMethods(n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]))   #Output: []