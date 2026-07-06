class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        start = 1
        while n >= start:
            n -= start
            count += 1
            start += 1
        return count
        
my_solution = Solution()
print(my_solution.arrangeCoins(5))         #Output: 2
                
            
            