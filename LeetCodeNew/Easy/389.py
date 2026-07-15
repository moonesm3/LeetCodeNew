class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in t: 
            if char not in seen or seen[char] == 0:
                return char
            else:
                seen[char] -= 1

my_solution = Solution()
print(my_solution.findTheDifference(s = "abcd", t = "abcde"))   #Output: e   