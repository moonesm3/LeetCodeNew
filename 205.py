class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check1, check2 = {}, {}
        for i in range(len(s)):
            char1, char2 = s[i], t[i]
            if char1 not in check1:
                check1[char1] = char2
            if char2 not in check2:
                check2[char2] = char1
            if check1[char1] != char2 or check2[char2] != char1:
                return False
        return True
    
my_solution = Solution()
print(my_solution.isIsomorphic(s = "egg", t = "add")) #Output: True
print(my_solution.isIsomorphic(s ="badc", t = "baba")) #Output: Flase