#Getting a bit of help from ChatGPT for better time complexity
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << seat)

        ans = 2 * (n - len(rows))
        left = sum(1 << i for i in range(2, 6))   
        middle = sum(1 << i for i in range(4, 8))    
        right = sum(1 << i for i in range(6, 10))   

        for mask in rows.values():
            left_free = (mask & left) == 0
            right_free = (mask & right) == 0
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or (mask & middle) == 0:
                ans += 1
        return ans


my_solution = Solution()
print(my_solution.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))   #Output: 4 
print(my_solution.maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))    #Output: 2
print(my_solution.maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))    #Output: 4
