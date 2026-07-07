class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        perimeter -= 1
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        perimeter -= 1
        return perimeter
                           
my_solution = Solution()
print(my_solution.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))    #Output: 16
print(my_solution.islandPerimeter(grid = [[1]]))    #Output: 4
print(my_solution.islandPerimeter( grid = [[1,0]]))    #Output: 4
