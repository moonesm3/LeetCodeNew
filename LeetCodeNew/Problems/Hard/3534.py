#For the logic check the challenge 3532.py
class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        output = []
        #Sort node indexes based on nums value
        order = sorted(range(n), key=lambda i: nums[i])
        sorted_nums = [nums[i] for i in order]
        rank = [0] * n
        
        for sorted_index, original_index in enumerate(order):
            rank[original_index] = sorted_index

        possibilities = [0] * n
        group = 0

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > maxDiff:
                group += 1
            possibilities[i] = group

        reach = [0] * n
        right = 0

        for left in range(n):
            if right < left:
                right = left
            while right + 1 < n and sorted_nums[right + 1] - sorted_nums[left] <= maxDiff:
                right += 1
            reach[left] = right
        LOG = n.bit_length()
        jump = [reach]

        for _ in range(1, LOG):
            previous = jump[-1]
            current = [0] * n
            for i in range(n):
                current[i] = previous[previous[i]]
            jump.append(current)
            
        for query in queries:
            i = query[0]
            j = query[1]
            left = rank[i]
            right = rank[j]
            if left == right:
                output.append(0)
                continue
            if left > right:
                left, right = right, left
            #No path exists so -1
            if possibilities[left] != possibilities[right]:
                output.append(-1)
                continue

            #Find minimum number of moves from left to right
            steps = 0
            current = left
            for power in range(LOG - 1, -1, -1):
                if jump[power][current] < right:
                    current = jump[power][current]
                    steps += 1 << power
            output.append(steps + 1)
        return output

    
my_solution = Solution()
print(my_solution.pathExistenceQueries(n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]))   #Output: [1,1]
print(my_solution.pathExistenceQueries( n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]))   #Output: [1,2,-1,1]
print(my_solution.pathExistenceQueries(n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]))   #Output: [0,-1,-1]


