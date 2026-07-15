#You can also solve this question by considering pivot = sqrt(n*(n+1)/2) --> Then get the int of pivot and see if the int value is equal to pivot or not.
class Solution:
    def pivotInteger(self, n: int) -> int:
        l = []
        for i in range(1,n+1):
            l.append(i)
        sum1 = 0
        sum2= 0
        for i in range(len(l)):
            sum1 += l[i]
            sum2 = sum(l[i::])
            if sum1 == sum2:
                return i+1
        return -1
        
    
    
my_solution = Solution()
print(my_solution.pivotInteger(8))
print(my_solution.pivotInteger(4))