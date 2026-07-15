import math
class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        output = []
        possibilites = [0] * n
        group = 0

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > maxDiff:
                group += 1
            possibilites[i] = group
            
        for querie in queries:
            i = querie[0]
            j = querie[1]
            if possibilites[i] == possibilites[j]:
                output.append(True)
            else:
                output.append(False)
        return output
    
my_solution = Solution()
print(my_solution.pathExistenceQueries(n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]))     #Output: [true,false]
print(my_solution.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]))     #Output: [false,false,true,true]