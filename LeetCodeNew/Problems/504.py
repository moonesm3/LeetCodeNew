class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        l = []
        while num >= 1:
            m = num % 7
            l.append(str(m))
            num = num // 7
        result = ''.join(reversed(l))
        if negative:
            return "-" + result
        return result  

my_solution = Solution()
print(my_solution.convertToBase7(100))   #Output: 202        
print(my_solution.convertToBase7(-7))   #Output: -10  