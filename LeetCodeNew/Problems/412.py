class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l = []
        for i in range(n):
            i += 1
            if (i % 3 == 0 and i % 5 == 0):
                l.append("FizzBuzz")             
            elif (i % 5 == 0):
                l.append("Buzz")
            elif (i % 3 == 0):
                l.append("Fizz")
            else:
                l.append(str(i))
        return l
    
my_solution = Solution()
print(my_solution.fizzBuzz(n = 3))
print(my_solution.fizzBuzz(n = 15))