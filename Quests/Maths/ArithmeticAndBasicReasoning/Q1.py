class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        dist = arr[1] - arr[0]
        l = []
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1] == dist):
                l.append(True)
            else: 
                l.append(False)
        if False in l:
            return False
        return True       
        
        
my_solution = Solution()
print(my_solution.canMakeArithmeticProgression(arr = [3,5,1]))  #Output: True
print(my_solution.canMakeArithmeticProgression(arr = [1,2,4]))  #Output: False