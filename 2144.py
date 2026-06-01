#Easy Problem: 2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if i < 2:
                total += cost[i]
            elif i % 3 == 0:
                total += cost[i]
            elif i % 3 == 1:
                total += cost[i]
        return total
    
my_solution = Solution()
print(my_solution.minimumCost([1, 2, 3])) # 5
print(my_solution.minimumCost([6,5,7,9,2,2])) 
print(my_solution.minimumCost([5,5])) # 10git branch -a