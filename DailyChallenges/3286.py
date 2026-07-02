import heapq
class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        damage = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        start = grid[0][0]
        damage[0][0] = start
        pq = []
        heapq.heappush(pq, (start, 0, 0))
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]
        while pq:
            current_damage, row, col = heapq.heappop(pq)
            if row == rows - 1 and col == cols - 1:
                return current_damage < health
            if current_damage > damage[row][col]:
                continue
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_damage = current_damage + grid[new_row][new_col]
                    # health must remain positive
                    if new_damage >= health:
                        continue
                    if new_damage < damage[new_row][new_col]:
                        damage[new_row][new_col] = new_damage
                        heapq.heappush(pq, (new_damage, new_row, new_col))
        return False
    
    
my_solution = Solution()
print(my_solution.findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1))    #Output: True
print(my_solution.findSafeWalk(grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3))    #Output: False
        