class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-"))
        s = s.upper()
        m = s[::-1]
        groups = []
        for i in range(0, len(m), k):
            groups.append(m[i:i+k])
        result = "-".join(groups)
        results = result[::-1]
        return str(results)
        


my_solution = Solution()
print(my_solution.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))  #Output: 5F3Z-2E9W
print(my_solution.licenseKeyFormatting(s = "2-5g-3-J", k = 2))  #Output: "2-5G-3J"