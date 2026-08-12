from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = Counter()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            freq[x] += 1
            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

my_solution = Solution()
print(my_solution.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))     #Output: 6
print(my_solution.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1))     #Output: 2
print(my_solution.maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4))     #Output: 4
