class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        length = 0
        for char in s:
            if char in unmatched:
                unmatched.remove(char)
                length += 2   #every set is two characters
            else:
                unmatched.add(char)
        if unmatched:
            length += 1

        return length
        
        
    
my_solution = Solution()
print(my_solution.longestPalindrome(s = "abccccdd"))