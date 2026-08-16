#Alice and Bob, please find another game....
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1

        c0, c1, c2 = count
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        else:
            return abs(c1 - c2) > 2


my_solution = Solution()
print(my_solution.stoneGameIX(stones = [2,1]))     #Output: True
print(my_solution.stoneGameIX(stones = [2]))     #Output: False
print(my_solution.stoneGameIX(stones = [5,1,2,4,3]))     #Output: False
