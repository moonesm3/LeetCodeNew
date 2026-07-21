class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active = s.count("1")
        extended = "1" + s + "1"
        zero_groups = []
        i = 0
        while i < len(extended):
            if extended[i] == "0":
                length = 0
                while i < len(extended) and extended[i] == "0":
                    length += 1
                    i += 1
                zero_groups.append(length)
            else:
                i += 1
                
        MaxActive = 0
        for i in range(1, len(zero_groups)):
            optimize = zero_groups[i - 1] + zero_groups[i]
            MaxActive = max(MaxActive, optimize)
        return active + MaxActive

my_solution = Solution()
print(my_solution.maxActiveSectionsAfterTrade(s = "01"))   #Output: 1
print(my_solution.maxActiveSectionsAfterTrade( s = "0100"))   #Output: 4