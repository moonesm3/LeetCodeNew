class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m = p
        n = q
        while m % 2 == 0 and n % 2 == 0:
            m //= 2
            n //= 2
        if m % 2 == 1 and n % 2 == 0:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        else:
            return 2

my_solution = Solution()
print(my_solution.mirrorReflection(p = 2, q = 1))   #Output: 2
print(my_solution.mirrorReflection(p = 3, q = 1))   #Output: 1