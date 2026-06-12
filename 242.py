class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = set(s)
        z = list(s)
        n = list(t)
        if (len(n) == len(z)):
            seen = set()
            for char in n:
                seen.add(char) 
            if m == seen:
                return True
        return False      
    
my_solution = Solution()
print(my_solution.isAnagram( s = "anagram", t = "nagaram"))   #Output: True
print(my_solution.isAnagram(s = "rat", t = "car"))   #Output: False
print(my_solution.isAnagram(s = "aacc", t = "ccac"))   #Output: False
print(my_solution.isAnagram(s = "aa", t = "a"))   #Output: False