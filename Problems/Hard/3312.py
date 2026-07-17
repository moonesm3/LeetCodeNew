#For this question, try not to generate all the pairs. Because you will have too many pairs that basically you will lose it! -->
#1. Count all pairs where both numbers are divisible by g.
#2. Remove pairs whose GCD is actually a larger multiple of g.
from bisect import bisect_right
class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:     
        max_num = max(nums)
        frequency = [0] * (max_num + 1)
        for num in nums:
            frequency[num] += 1
            
        #Number of pairs
        gcd_count = [0] * (max_num + 1)
        #Inclusion-exclusion --> As suggested by the hint
        for g in range(max_num, 0, -1):
            divisible_count = 0
            #Point 1
            for multiple in range(g, max_num + 1, g):
                divisible_count += frequency[multiple]
            pairs = (divisible_count * (divisible_count - 1)// 2)
            #Point 2
            for multiple in range(2 * g, max_num + 1, g):
                pairs -= gcd_count[multiple]
            gcd_count[g] = pairs

        prefix = [0] * (max_num + 1)
        for g in range(1, max_num + 1): prefix[g] = (prefix[g - 1] + gcd_count[g])
        answer = []
        for query in queries:
            gcd_value = bisect_right(prefix, query)
            answer.append(gcd_value)
        return answer
    
    
my_solution = Solution()
print(my_solution.gcdValues(nums = [2,3,4], queries = [0,2,2]))     #Output: [1,2,2]
print(my_solution.gcdValues(nums = [4,4,2,1], queries = [5,3,1,0]))     #Output: [4,2,1,1] --> 6 pairs
print(my_solution.gcdValues(nums = [2,2], queries = [0,0]))     #Output: [2,2]