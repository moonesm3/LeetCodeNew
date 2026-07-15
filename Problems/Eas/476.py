class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = ""
        for i in range(len(binary)):
            if binary[i] == "0":
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)
               
my_solution = Solution()
print(my_solution.findComplement(5))      #Output: 2