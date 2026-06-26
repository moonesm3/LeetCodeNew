class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        l = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                l.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return l
    
my_solution = Solution()
print(my_solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(my_solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))