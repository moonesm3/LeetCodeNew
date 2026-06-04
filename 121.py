class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

my_solution = Solution()
print(my_solution.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(my_solution.maxProfit([1, 2, 3, 4, 5])) # 4
print(my_solution.maxProfit([2,4,1])) # 2      