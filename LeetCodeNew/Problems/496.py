class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        for item in nums1:
            index = nums2.index(item)
            found = False

            for i in range(index + 1, len(nums2)):
                if nums2[i] > item:
                    output.append(nums2[i])
                    found = True
                    break
            if not found:
                output.append(-1)
        return output                      
        
my_solution = Solution()
print(my_solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))    #Output: [-1,3,-1]
print(my_solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))   #Output: [3,-1]