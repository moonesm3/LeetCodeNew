class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        total = 0
        count = 0
        costs.sort()
        for cost in costs:
            if total + cost > coins:
                break
            total += cost
            count += 1
        return count
    
my_solution = Solution()
print(my_solution.maxIceCream(costs = [1,3,2,4,1], coins = 7))     #Output: 4
            
        