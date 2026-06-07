class Solution:
    def hammingWeight(self, n: int) -> int:
        m = format(n, 'b')
        count = 0
        z = [j for i in m for j in i]
        # print(z)
        for i in z:
            i = int(i)
            if (i == 1):
                count += 1
        return count
    


my_solution = Solution()
print(my_solution.hammingWeight(11)) #Output: 3
print(my_solution.hammingWeight(128)) #Output: 1 