#In Amazon --> you can go by order of the char too and not using them directly
#This is not a medium problem....
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        letters = sorted(count.keys())

        def remaining_string():
            result = ""
            for ch in letters:
                result += ch * count.get(ch, 0)
            return result

        def backtrack(i):
            if i == len(target):
                return None
            if count.get(target[i], 0) > 0:
                count[target[i]] -= 1
                suffix = backtrack(i + 1)
                if suffix is not None:
                    return target[i] + suffix
                count[target[i]] += 1
            for ch in letters:
                if ch > target[i] and count.get(ch, 0) > 0:
                    count[ch] -= 1
                    answer = ch + remaining_string()
                    count[ch] += 1
                    return answer
            return None
        answer = backtrack(0)
        return answer if answer is not None else ""


my_solution = Solution()
print(my_solution.lexGreaterPermutation(s = "abc", target = "bba"))     #Output: "bca"
print(my_solution.lexGreaterPermutation(s = "leet", target = "code"))     #Output: "eelt"
print(my_solution.lexGreaterPermutation(s = "baba", target = "bbaa"))     #Output: ""