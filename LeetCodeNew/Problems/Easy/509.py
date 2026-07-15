class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        
my_solution = Solution()
print(my_solution.fib(2))    #Output: 1
print(my_solution.fib(3))    #Output: 2
print(my_solution.fib(4))    #Output: 3
    
