class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            if gap >= duration:
                total += duration
            else:
                total += gap
        total += duration
        return total


my_solution = Solution()
print(my_solution.findPoisonedDuration(timeSeries = [1,4], duration = 2))     #Output: 4
print(my_solution.findPoisonedDuration(timeSeries = [1,2], duration = 2))     #Output: 3