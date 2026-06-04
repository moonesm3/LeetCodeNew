class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        m = digits[-1]
        if m < 9:
            digits[-1] = m + 1
            return digits
        else:
            digits[-1] = 0
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
            return [1] + digits
    
my_solution = Solution()
print(my_solution.plusOne([1, 2, 3])) # [1, 2, 4]
print(my_solution.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
print(my_solution.plusOne([9])) # [1, 0]    