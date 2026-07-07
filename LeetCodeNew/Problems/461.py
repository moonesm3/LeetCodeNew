class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num1 = bin(x)[2:]   
        num2 = bin(y)[2:] 
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num2) < len(num1):
            num2 = "0" + num2
        distance = 0 
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                distance += 1
        return distance

my_solution = Solution()
print(my_solution.hammingDistance(x = 1, y = 4))     #Output: 2
print(my_solution.hammingDistance(x = 3, y = 1))     #Output: 1

#Better solution may be to use: bitwise XOR and bit counts