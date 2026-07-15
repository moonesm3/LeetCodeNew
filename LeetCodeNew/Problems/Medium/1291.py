class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        n = "123456789"
        l = []
        output = []
        for i in range(len(n)):
            for j in range(i + 1, len(n) + 1):
                l.append(n[i:j])
        for item in l:
            number = int(item)
            if number >= low and number <= high:
                output.append(number)
        output.sort()
        return output
                
                
my_solution = Solution()
print(my_solution.sequentialDigits(low = 100, high = 300))   #Output:  [123,234]
print(my_solution.sequentialDigits(low = 89, high = 234))   #Output:  [89,123,234]

        