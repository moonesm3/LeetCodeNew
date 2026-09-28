class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxCounter = 0
        for i in s:
            if i == "(":
                counter += 1
                maxCounter = max(maxCounter, counter)
            elif i == ")":
                counter -= 1
        return maxCounter
    
my_solution = Solution()
print(my_solution.maxDepth("(1+(2*3)+((8)/4))+1"))    #Output: 3
    