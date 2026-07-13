class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        l = []
        sc = sorted(score, reverse=True)
        for i in range(len(score)):
            rank = sc.index(score[i]) + 1
            if rank == 1:
                l.append("Gold Medal")
            elif rank == 2:
                l.append("Silver Medal")
            elif rank == 3:
                l.append("Bronze Medal")
            else:
                l.append(str(rank))
        return l
                
my_solution = Solution()
print(my_solution.findRelativeRanks([10,3,8,9,4]))       #Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        