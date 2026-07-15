class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for number in range(left, right + 1):
            is_self_dividing = True
            for char in str(number):
                digit = int(char)
                if digit == 0 or number % digit != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                result.append(number)
        return result
        
        
my_solution = Solution()
print(my_solution.selfDividingNumbers(left = 1, right = 22))   #Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]