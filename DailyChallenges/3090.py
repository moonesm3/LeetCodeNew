#Solving by sliding window
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        count = {}
        max_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

my_solution = Solution()
print(my_solution.maximumLengthSubstring(s = "bcbbbcba"))     #Output: 4
print(my_solution.maximumLengthSubstring(s = "aaaa"))     #Output: 2