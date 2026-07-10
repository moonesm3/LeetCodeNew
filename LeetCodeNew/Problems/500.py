class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []
        
        for word in words:
            lower_word = word.lower()
            if all(char in row1 for char in lower_word):
                result.append(word)
            elif all(char in row2 for char in lower_word):
                result.append(word)
            elif all(char in row3 for char in lower_word):
                result.append(word)
        return result
    
my_solution = Solution()
print(my_solution.findWords(words = ["Hello","Alaska","Dad","Peace"]))     #Output: ["Alaska","Dad"]
print(my_solution.findWords(words = ["omk"]))     #Output: []
print(my_solution.findWords(words = ["adsdf","sfd"]))     #Output: ["adsdf","sfd"]

        