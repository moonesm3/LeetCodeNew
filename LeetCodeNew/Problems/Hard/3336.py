from math import gcd
class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        dp = {(0, 0): 1}
             
        for num in nums:
            new_dp = {}
            for (gcd1, gcd2), count in dp.items():
                state = (gcd1, gcd2)
                new_dp[state] = (new_dp.get(state, 0) + count) % MOD
                new_gcd1 = gcd(gcd1, num)
                state = (new_gcd1, gcd2)
                new_dp[state] = (new_dp.get(state, 0) + count) % MOD
                new_gcd2 = gcd(gcd2, num)
                state = (gcd1, new_gcd2)
                new_dp[state] = (new_dp.get(state, 0) + count) % MOD
            dp = new_dp
            
        answer = 0
        for (gcd1, gcd2), count in dp.items():
            if gcd1 != 0 and gcd1 == gcd2:
                answer = (answer + count) % MOD
        return answer
        
        
my_solution = Solution()
print(my_solution.subsequencePairCount(nums = [1,2,3,4]))    #Output: 10
print(my_solution.subsequencePairCount(nums = [10,20,30]))    #Output: 2
print(my_solution.subsequencePairCount( nums = [1,1,1,1]))    #Output: 50