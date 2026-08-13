#Study about segment tree!!
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        s = list(s)
        best = [0] * (4 * n)
        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        length = [0] * (4 * n)

        def build(node, left, right):
            length[node] = right - left + 1
            if left == right:
                best[node] = 1
                prefix[node] = 1
                suffix[node] = 1
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            merge(node, left, mid, right)

        def merge(node, left, mid, right):
            L = node * 2
            R = node * 2 + 1
            best[node] = max(best[L], best[R])
            prefix[node] = prefix[L]
            suffix[node] = suffix[R]
            if s[mid] == s[mid + 1]:
                combined = suffix[L] + prefix[R]
                best[node] = max(best[node], combined)
                if prefix[L] == length[L]:
                    prefix[node] += prefix[R]
                if suffix[R] == length[R]:
                    suffix[node] += suffix[L]

        def update(node, left, right, index):
            if left == right:
                return

            mid = (left + right) // 2
            if index <= mid:
                update(node * 2, left, mid, index)
            else:
                update(node * 2 + 1, mid + 1, right, index)
            merge(node, left, mid, right)

        build(1, 0, n - 1)
        answer = []
        for char, index in zip(queryCharacters, queryIndices):
            s[index] = char
            update(1, 0, n - 1, index)
            answer.append(best[1])
        return answer



my_solution = Solution()
print(my_solution.longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]))    #Output: [3, 3, 4]
print(my_solution.longestRepeating(s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]))    #Output: [2, 3]