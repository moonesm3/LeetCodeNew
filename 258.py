class Solution:
    def addDigits(self, num: int) -> int:
        while (num >= 10):
            l = [int(i) for i in str(num)]
            #print(l)
            sum = 0
            for i in range(len(l)):
                sum += l[i]
                #print(sum)
            num = sum          
        else:
            return num
        
my_solution = Solution()
print(my_solution.addDigits(38))   #Output: 2
print(my_solution.addDigits(10))   #Output: 1 
print(my_solution.addDigits(30))   #Output: 3 