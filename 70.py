# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = 0
        a, b = 1, 2
        for i in range(3, n + 1):
            while n > 2:
                ways = a + b
                a, b = b, ways
                n -= 1              
        return ways
my_solution = Solution()
print(my_solution.climbStairs(2)) # 2
print(my_solution.climbStairs(3)) # 3
print(my_solution.climbStairs(4)) # 5