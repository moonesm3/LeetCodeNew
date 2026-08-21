#Using ChatGPT for the solving the time complexity problem
from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins.sort()
        filtered = []
        for coin in coins:
            if not any(coin % x == 0 for x in filtered):
                filtered.append(coin)

        coins = filtered
        m = len(coins)
        subsets = []

        for mask in range(1, 1 << m):
            lcm = 1
            bits = 0
            for i in range(m):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm * coins[i] // gcd(lcm, coins[i])

            sign = 1 if bits % 2 == 1 else -1
            subsets.append((lcm, sign))

        def count(x):
            total = 0
            for lcm, sign in subsets:
                if lcm <= x:
                    total += sign * (x // lcm)
            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left


my_solution = Solution()
print(my_solution.findKthSmallest(coins = [3,6,9], k = 3))      #Output: 9
print(my_solution.findKthSmallest(coins = [5,2], k = 7))      #Output: 12
