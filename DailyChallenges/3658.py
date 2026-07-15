from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        Odd = []
        Even = []
        for i in range(1,n+n+1):
            if (i % 2 == 0):
                Even.append(i)
            else:
                Odd.append(i)
        odd = sum(Odd)
        even = sum(Even)
        gccd = gcd(odd, even)
        return gccd
            
my_solution = Solution()
print(my_solution.gcdOfOddEvenSums(4))