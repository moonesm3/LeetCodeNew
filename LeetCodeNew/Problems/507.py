class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        #Always 1
        divisors_sum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
            i += 1
        return divisors_sum == num
        
my_solution = Solution()
print(my_solution.checkPerfectNumber(28))    #Output: True
print(my_solution.checkPerfectNumber(7))   #Output: False