import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

my_solution = Solution()
print(my_solution.majorityElement([3,2,3]))
