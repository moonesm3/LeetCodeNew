import math
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        x = int(math.sqrt(area))
        for i in range(x, 0, -1):
            if area % i == 0:
                W = i
                L = area // i
                return [L, W]
            


my_solution = Solution()
print(my_solution.constructRectangle(4))   #Output: [2,2]
print(my_solution.constructRectangle(37))   #Output: [37,1]
print(my_solution.constructRectangle(122122))   #Output: [427,286]