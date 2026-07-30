class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        for i in range(len(word)):
            pushes += i // 8 + 1
            #print(pushes)
        return pushes
    

my_solution = Solution()
print(my_solution.minimumPushes(word = "abcde"))    #Output: 5
print(my_solution.minimumPushes(word = "xycdefghij"))    #Output: 12
