class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        answer = 0
        def dfs(node):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        for node in range(n):
            if visited[node]:
                continue

            component = []
            dfs(node)
            size = len(component)
            complete = True
            for node in component:
                if len(graph[node]) != size - 1:
                    complete = False
                    break
            if complete:
                answer += 1
        return answer

        
my_solution = Solution()
print(my_solution.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))   #Output: 3