#See Problem 3754 to know more about the logic
class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        count_nonzero = [0] * (n + 1)
        prefix_value = [0]
        prefix_sum = [0]

        # 10 ** i modulo MOD
        pow10 = [1]
        nonzero_count = 0

        for i, ch in enumerate(s):
            if ch != "0":
                digit = ord(ch) - ord("0")
                nonzero_count += 1
                prefix_value.append((prefix_value[-1] * 10 + digit) % MOD)
                prefix_sum.append(prefix_sum[-1] + digit)
                pow10.append((pow10[-1] * 10) % MOD)
            count_nonzero[i + 1] = nonzero_count
            
        answers = []
        for left, right in queries:
            start = count_nonzero[left]
            end = count_nonzero[right + 1]
            length = end - start
            if length == 0:
                answers.append(0)
                continue
            x = (prefix_value[end] - prefix_value[start] * pow10[length]) % MOD
            digit_sum = prefix_sum[end] - prefix_sum[start]
            answers.append((x * digit_sum) % MOD)
        return answers
    
    
my_solution = Solution()
print(my_solution.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]]))     #Output: [12340, 4, 9]
print(my_solution.sumAndMultiply(s = "1000", queries = [[0,3],[1,1]]))     #Output: [1, 0]
print(my_solution.sumAndMultiply(s = "9876543210", queries = [[0,9]]))     #Output: [444444137]