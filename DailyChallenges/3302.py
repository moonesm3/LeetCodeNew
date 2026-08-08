class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)
        if n < m:
            return []
        suffix = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suffix[i] = m - 1 - j

        answer = []
        j = 0
        mismatch_used = False

        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                answer.append(i)
                j += 1
            elif not mismatch_used:
                remaining = m - j - 1
                if suffix[i + 1] >= remaining:
                    answer.append(i)
                    j += 1
                    mismatch_used = True
        if len(answer) == m:
            return answer                         
        return []


my_solution = Solution()
print(my_solution.validSequence(word1 = "vbcca", word2 = "abc"))     #Output: [0, 1, 2]
print(my_solution.validSequence(word1 = "bacdc", word2 = "abc"))     #Output: [1, 2, 4]
print(my_solution.validSequence(word1 = "aaaaaa", word2 = "aaabc"))     #Output: []
print(my_solution.validSequence(word1 = "abc", word2 = "ab"))     #Output: [0, 1]