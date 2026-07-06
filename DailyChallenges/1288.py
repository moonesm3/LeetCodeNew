class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        for i in range(len(intervals)):
            covered = False
            for j in range(len(intervals)):
                if i != j:
                    if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                        covered = True
            if not covered:
                count += 1
        return count
              
            
my_solution = Solution()
print(my_solution.removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]]))    #Output: 2
print(my_solution.removeCoveredIntervals(intervals = [[1,4],[2,3]]))    #Output: 1