class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = min(nums1)
        #We cannot make all the numbers even 
        if minimum % 2 == 1:
            return True
        for num in nums1:
            if num % 2 == 1:
                return False
        return True


my_solution = Solution()
print(my_solution.uniformArray(nums1 = [1,4,7]))    #Output: True
print(my_solution.uniformArray(nums1 = [2,3]))    #Output: False
print(my_solution.uniformArray(nums1 = [4,6]))    #Output: True