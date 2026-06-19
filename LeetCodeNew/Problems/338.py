#Brian Kernighan’s Algorithm
class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for number in range(n + 1):
            count = 0
            x = number
            while x != 0:
                x = x & (x - 1)
                count += 1
            result.append(count)
        return result

my_solution = Solution()
print(my_solution.countBits(13))
print(my_solution.countBits(2))