class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2


my_solution = Solution()
print(my_solution.resultArray(nums = [2,1,3]))     #Output: [2,3,1]
print(my_solution.resultArray(nums = [5,4,3,8]))     #Output: [5,3,4,8]