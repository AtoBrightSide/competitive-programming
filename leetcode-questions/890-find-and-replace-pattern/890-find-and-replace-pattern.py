class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def checker(word):
            replace_word, replace_pattern = {}, {}
            for i, letter in enumerate(pattern):
                if letter in replace_word and replace_word[letter] != word[i]:  return False
                if word[i] in replace_pattern and replace_pattern[word[i]] != letter:   return False
                
                replace_word[letter] = word[i]
                replace_pattern[word[i]] = letter
                
            return True
        
        matches = []
        for word in words:
            if checker(word):   matches.append(word)
                
        return matches
            