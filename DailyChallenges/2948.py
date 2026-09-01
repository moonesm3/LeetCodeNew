class Solution:
    def lexicographicallySmallestArray(
        self, nums: list[int], limit: int) -> list[int]:

        pairs = []
        for i in range(len(nums)):
            pairs.append((nums[i], i))
        pairs.sort()

        answer = nums[:]
        start = 0
        for i in range(1, len(pairs) + 1):
            if i == len(pairs) or pairs[i][0] - pairs[i - 1][0] > limit:
                group = pairs[start:i]
                values = []
                indices = []
                for value, index in group:
                    values.append(value)
                    indices.append(index)
                indices.sort()
                for j in range(len(group)):
                    answer[indices[j]] = values[j]
                start = i
        return answer

my_solution = Solution()
print(my_solution.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2))     #Output: [1,3,5,8,9]
print(my_solution.lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3))     #Output: [1,6,7,18,1,2]
print(my_solution.lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3))     #Output: [[1,7,28,19,10]
