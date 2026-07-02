class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if (s.count(char) == 1):
                return s.index(char)
        return -1 
            
            
my_solution = Solution()
print(my_solution.firstUniqChar("leetcode"))    #Output: 0
print(my_solution.firstUniqChar("loveleetcode"))    #Output: 2