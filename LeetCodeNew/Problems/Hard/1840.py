# 1840. Maximum Building Height
# Second day Challenge
class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions = [[1, 0]] + sorted(restrictions) + [[n, n - 1]]

        for i in range(1, len(restrictions)):
            distance = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + distance)

        for i in range(len(restrictions) - 2, -1, -1):
            distance = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + distance)

        MaxDistance = 0
        for i in range(1, len(restrictions)):
            left_id, left_h = restrictions[i - 1]
            right_id, right_h = restrictions[i]
            distance = right_id - left_id
            mean = (left_h + right_h + distance) // 2
            MaxDistance = max(MaxDistance, mean)
        return MaxDistance
    
my_solution = Solution()
print(my_solution.maxBuilding(n = 5, restrictions = [[2,1],[4,1]]))   #Output: 2
print(my_solution.maxBuilding(n = 6, restrictions = []))     #Output: 5