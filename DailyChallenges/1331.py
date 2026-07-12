class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(set(arr))
        rank = {}
        for i in range(len(sorted_unique)):
            rank[sorted_unique[i]] = i + 1
        result = []
        for num in arr:
            result.append(rank[num])
        return result
    

my_solution = Solution()
print(my_solution.arrayRankTransform(arr = [40,10,20,30]))      #Output: [4,1,2,3]