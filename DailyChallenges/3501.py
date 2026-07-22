from bisect import bisect_left, bisect_right
#Using ChatGPT fpr sure to understand how to solve the timelimit problem :))) --> Check 2499.py to see the semi-solution with runtime
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        total_ones = s.count("1")
        starts = []
        ends = []
        lengths = []
        i = 0
        while i < len(s):
            if s[i] == "1":
                i += 1
                continue
            start = i
            while i < len(s) and s[i] == "0":
                i += 1
            end = i - 1
            starts.append(start)
            ends.append(end)
            lengths.append(end - start + 1)
        zero_count = len(lengths)
        if zero_count < 2:
            return [total_ones] * len(queries)
        pair_sum = [lengths[i] + lengths[i + 1] for i in range(zero_count - 1)]
        m = len(pair_sum)
        levels = m.bit_length()
        table = [pair_sum[:]]
        for level in range(1, levels):
            size = 1 << level
            half = size // 2
            previous = table[level - 1]
            current = [0] * m
            for j in range(m - size + 1):
                current[j] = max(previous[j], previous[j + half])
            table.append(current)
            
        def range_max(left: int, right: int) -> int:
            if left > right:
                return 0
            length = right - left + 1
            level = length.bit_length() - 1
            size = 1 << level
            return max(table[level][left], table[level][right - size + 1])
        
        def overlap_length(group_index: int, query_left: int, query_right: int) -> int:
            left = max(starts[group_index], query_left)
            right = min(ends[group_index], query_right)
            if left > right:
                return 0
            return right - left + 1
        answer = []
        for left, right in queries:
            first_group = bisect_left(ends, left)
            last_group = bisect_right(starts, right) - 1
            if (first_group >= zero_count or last_group < 0 or first_group >= last_group):
                answer.append(total_ones)
                continue
            best_gain = 0
            gain = (overlap_length(first_group, left, right) + overlap_length(first_group + 1, left, right))
            best_gain = max(best_gain, gain)
            gain = (overlap_length(last_group - 1, left, right) + overlap_length(last_group, left, right))
            best_gain = max(best_gain, gain)
            internal_left = first_group + 1
            internal_right = last_group - 2
            best_gain = max(best_gain, range_max(internal_left, internal_right))
            answer.append(total_ones + best_gain)
        return answer
   
my_solution = Solution()
print(my_solution.maxActiveSectionsAfterTrade(s = "01", queries = [[0,1]]))  #Output: [1]
print(my_solution.maxActiveSectionsAfterTrade(s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]))  #Output: [4,3,1,1]