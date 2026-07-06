class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
  
my_solution = Solution()
print(my_solution.isSubsequence(s = "abc", t = "ahbgdc"))    #True       
print(my_solution.isSubsequence(s = "axc", t = "ahbgdc"))    #False
print(my_solution.isSubsequence(s = "aaa", t = "aabcd"))    #False