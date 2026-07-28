class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        m = len(s)
        l = []
        for i in range(m // 2):
            l.append(s[i])
        l.sort()
        left = "".join(l)
        if m % 2 == 1:
            z = s[m // 2]
        else:
            z = ""
        return left + z + left[::-1]
            
            
my_solution = Solution()
print(my_solution.smallestPalindrome(s = "babab"))   #Output: "abbba"
print(my_solution.smallestPalindrome(s = "daccad"))   #Output: "acddca"