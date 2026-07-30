from collections import Counter
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = s[:n // 2]
        count = Counter(half)
        middle = s[n // 2] if n % 2 == 1 else ""
        def count_permutations(limit):
            ways = 1
            used = 0
            for amount in count.values():
                ways *= comb(used + amount, amount)
                used += amount
                if ways >= limit:
                    return limit
            return ways
        if count_permutations(k) < k:
            return ""
        left = []
        remaining = len(half)
        while remaining > 0:
            for char in sorted(count):
                if count[char] == 0:
                    continue
                count[char] -= 1
                ways = count_permutations(k)
                if ways >= k:
                    left.append(char)
                    remaining -= 1
                    break
                k -= ways
                count[char] += 1
        left = "".join(left)
        return left + middle + left[::-1]
                       
my_solution = Solution()
print(my_solution.smallestPalindrome(s = "abba", k = 2))   #Output: "baab"
print(my_solution.smallestPalindrome(s = "aa", k = 2))   #Output: ""