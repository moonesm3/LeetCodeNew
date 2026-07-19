class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {char: i for i, char in enumerate(s)}
        stack = []
        used = set()
        for i, char in enumerate(s):
            if char in used:
             continue
            while stack and char < stack[-1] and last[stack[-1]] > i:
                used.remove(stack.pop())
            stack.append(char)
            used.add(char)
        return "".join(stack)
    

my_solution = Solution()
print(my_solution.smallestSubsequence(s = "bcabc"))     #Output: "abc"
print(my_solution.smallestSubsequence(s = "cbacdcbc"))     #Output: "dcbc"