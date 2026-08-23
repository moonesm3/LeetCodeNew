class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum = right_sum = 0
        left_q = right_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        total_q = left_q + right_q

        if total_q % 2 == 1:
            return True

        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)


my_solution = Solution()
print(my_solution.sumGame(num = "5023"))    #Output: False
print(my_solution.sumGame(num = "25??"))    #Output: True
print(my_solution.sumGame(num = "?3295???"))    #Output: False

