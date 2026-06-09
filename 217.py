class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

my_solution = Solution()
print(my_solution.containsDuplicate([1,2,3,1]))  #Output: True
print(my_solution.containsDuplicate([1,2,3,4]))  #Output: False
            