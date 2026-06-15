class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}

        slow = 0
        fast = 0

        while slow < len(pattern) and fast < len(words):
            char = pattern[slow]
            word = words[fast]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
            slow += 1
            fast += 1
        return True
    
my_solution = Solution()
print(my_solution.wordPattern(pattern = "abba", s = "dog cat cat dog"))   #Output: True
print(my_solution.wordPattern(pattern = "abba", s = "dog cat cat fish"))   #Output: False
print(my_solution.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))   #Output: False