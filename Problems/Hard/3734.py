#See 3720.py before seeing this solution. You will understand better.
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        #To check the possibility of palindrome
        odd = []
        for ch in count:
            if count[ch] % 2 == 1:
                odd.append(ch)
        if len(odd) > 1:
            return ""
        middle = odd[0] if odd else ""

        #Use half of each character
        half_count = {}
        for ch in count:
            half_count[ch] = count[ch] // 2
        letters = sorted(half_count.keys())
        half_length = len(s) // 2
        path = []

        def make_palindrome(left):
            return left + middle + left[::-1]

        def remaining_half():
            result = []
            for ch in letters:
                result.extend([ch] * half_count[ch])
            return "".join(result)

        def backtrack(i):
            if i == half_length:
                left = "".join(path)
                palindrome = make_palindrome(left)
                if palindrome > target:
                    return palindrome
                return None
            
            ch = target[i]
            if half_count.get(ch, 0) > 0:
                half_count[ch] -= 1
                path.append(ch)
                result = backtrack(i + 1)
                if result is not None:
                    return result

                path.pop()
                half_count[ch] += 1

            for ch in letters:
                if ch > target[i] and half_count.get(ch, 0) > 0:
                    half_count[ch] -= 1
                    path.append(ch)
                    left = "".join(path) + remaining_half()
                    palindrome = make_palindrome(left)
                    path.pop()
                    half_count[ch] += 1
                    return palindrome
            return None

        answer = backtrack(0)
        return answer if answer is not None else ""


my_solution = Solution()
print(my_solution.lexPalindromicPermutation(s = "baba", target = "abba"))    #Output: "baab"
print(my_solution.lexPalindromicPermutation(s = "baba", target = "bbaa"))    #Output: ""
print(my_solution.lexPalindromicPermutation(s = "abc", target = "abb"))    #Output: ""
print(my_solution.lexPalindromicPermutation(s = "aac", target = "abb"))    #Output: "aca"