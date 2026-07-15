class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        if k == 1:
            pattern = ["."]
        elif k == 2:
            if m < 2 or n < 2:
                return []
            pattern = ["..", ".."]
        elif k == 3:
            if m >= 2 and n >= 3:
                pattern = ["...", "..."]
            elif m >= 3 and n >= 2:
                pattern = ["..", "..", ".."]
            else:
                return []
        elif k == 4:
            if m >= 2 and n >= 4:
                pattern = ["....", "...."]
            elif m >= 4 and n >= 2:
                pattern = ["..", "..", "..", ".."]
            elif m >= 3 and n >= 3:
                pattern = ["..#", "...", "#.."]
            else:
                return []
        else:
            return []

        grid = [["#"] * n for _ in range(m)]
        rows = len(pattern)
        cols = len(pattern[0])
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = pattern[i][j]
        exit_row = rows - 1
        exit_col = cols - 1
        for col in range(exit_col, n):
            grid[exit_row][col] = "."
        for row in range(exit_row, m):
            grid[row][n - 1] = "."
        return ["".join(row) for row in grid]
    
    
my_solution = Solution()
print(my_solution.createGrid(m = 2, n = 3, k = 2))   #Output: ["...","#.."]
print(my_solution.createGrid(m = 3, n = 3, k = 4))   #Output: ["..#","...","#.."]