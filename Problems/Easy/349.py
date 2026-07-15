class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    if nums1[i] not in l:
                        l.append(nums1[i])
        return l

my_solution = Solution()
print(my_solution.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(my_solution.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))