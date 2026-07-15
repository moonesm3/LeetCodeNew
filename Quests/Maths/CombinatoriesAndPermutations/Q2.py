# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            if triangle:
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
            triangle.append(row)
        return triangle
    
    
my_solution = Solution()
print(my_solution.generate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(my_solution.generate(1)) # [[1]]