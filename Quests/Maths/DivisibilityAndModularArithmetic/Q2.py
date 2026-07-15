class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
    
    
my_solution = Solution()
print(my_solution.smallestRepunitDivByK(3))  #Output: 3  --> 111
print(my_solution.smallestRepunitDivByK(2))  #Output: -1 