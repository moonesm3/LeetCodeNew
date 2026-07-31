#See 3014.py for inspiration. --> This time the letters are not distinct
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(),reverse=True)
        pushes = 0
        for i, frequency in enumerate(frequencies):
            cost = i // 8 + 1
            pushes += frequency * cost
        return pushes
    

my_solution = Solution()
print(my_solution.minimumPushes(word = "abcde"))      #Output: 5
print(my_solution.minimumPushes(word = "xyzxyzxyzxyz"))      #Output: 12
print(my_solution.minimumPushes(word = "aabbccddeeffgghhiiiiii"))      #Output: 24
