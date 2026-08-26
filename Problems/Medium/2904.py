#In order to improve the code time and memory wise, I asked ChatGPT.
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(len(s)):
            if s[i] == "1":
                ones.append(i)

        if len(ones) < k:
            return ""

        answer = ""
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            string = s[start:end + 1]
            
            if answer == "":
                answer = string
            elif len(string) < len(answer):
                answer = string
            elif len(string) == len(answer) and string < answer:
                answer = string
        return answer
            
my_solution = Solution()
print(my_solution.shortestBeautifulSubstring(s = "100011001", k = 3))   #Output: "11001"
print(my_solution.shortestBeautifulSubstring(s = "1011", k = 2))   #Output: "11"
print(my_solution.shortestBeautifulSubstring(s = "000", k = 1))   #Output: ""


#First version of the code
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answer = ""
        for i in range(len(s)):
            string = ""
            count = 0
            for j in range(i, len(s)):
                if s[j] == "1":
                    count += 1
                string = string + s[j]
                if count == k:
                    if answer == "":
                        answer = string
                    elif len(string) < len(answer):
                        answer = string
                    elif len(string) == len(answer) and string < answer:
                        answer = string
                elif count > k:
                    break
        return answer