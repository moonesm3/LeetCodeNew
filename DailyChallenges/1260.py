class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                old_index = row * cols + col
                new_index = (old_index + k) % total
                new_row = new_index // cols
                new_col = new_index % cols
                result[new_row][new_col] = grid[row][col]
        return result
    
my_solution = Solution()
print(my_solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))   #Output: [[9,1,2],[3,4,5],[6,7,8]]
print(my_solution.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))   #Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print(my_solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))   #Output: [[1,2,3],[4,5,6],[7,8,9]]