class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        #Used guide from the discussion section
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            instability = prefix_max - suffix_min[i]
            if instability <= k:
                return i
        return -1


my_solution = Solution()
print(my_solution.firstStableIndex(nums = [5,0,1,4], k = 3))    #Output: 3
print(my_solution.firstStableIndex(nums = [3,2,1], k = 1))    #Output: -1
print(my_solution.firstStableIndex(nums = [0], k = 0))    #Output: 0