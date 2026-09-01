class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        left = min(min_index, max_index)
        right = max(min_index, max_index)
        from_front = right + 1
        from_back = n - left
        both_sides = (left + 1) + (n - right)
        return min(from_front, from_back, both_sides)

my_solution = Solution()
print(my_solution.minimumDeletions(nums = [2,10,7,5,4,1,8,6]))    #Output: 5
print(my_solution.minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))    #Output: 3
print(my_solution.minimumDeletions(nums = [101]))    #Output: 1
