class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g, reverse = False)
        s = sorted(s, reverse = False)      
        i = 0  
        j = 0
        while i < len(g) and j < len(s):
            if (g[i] <= s[j]):
                i += 1
            j += 1
        return i
                    
        
my_solution = Solution()
print(my_solution.findContentChildren( g = [1,2], s = [1,2,3]))    #Output: 3
        