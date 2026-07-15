# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num3 = nums1.copy()
        nums1.clear()
        for i in range(m):
            nums1.append(num3[i])
        for i in range(n):
            nums1.append(nums2[i])
            nums1.sort()
        return nums1
my_solution = Solution()
print(my_solution.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)) # [1,2,2,3,5,6]
print(my_solution.merge([1], 1, [], 0)) # [1]