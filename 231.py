class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = abs(n)
        m = bin(n)[2:]   
        l = [j for i in m for j in i]
        z = []
        for i in range(len(l)):
            if (l[i] == "1"):
                z.append(l[i])
        if (len(z) == 1):
            return True
        return False
                
        


my_solution = Solution()
print(my_solution.isPowerOfTwo(2)) #True
print(my_solution.isPowerOfTwo(-16)) #True
print(my_solution.isPowerOfTwo(5)) #False