class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = []
        for i in range(rowIndex + 1):
            row = [1]
            if triangle:
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
            triangle.append(row)
        return triangle[rowIndex]
my_solution = Solution()
print(my_solution.getRow(3)) # [1, 3, 3, 1]
print(my_solution.getRow(0)) # [1]
print(my_solution.getRow(1)) # [1, 1]