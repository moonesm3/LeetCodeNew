class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 2: 
            return length
        return 2 ** length.bit_length()
    
    
my_solution = Solution()
print(my_solution.uniqueXorTriplets(nums = [1,2]))    #Output: 2
print(my_solution.uniqueXorTriplets(nums = [3,1,2]))    #Output: 4