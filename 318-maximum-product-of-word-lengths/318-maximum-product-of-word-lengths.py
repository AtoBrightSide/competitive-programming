class Solution:
    def maxProduct(self, words: List[str]) -> int:
        best = 0
        
        wordlist = []
        for word in words:
            curr = [0] * 26
            for ch in word:
                curr[ord(ch) - ord('a')] = 1
            wordlist.append(curr)
            
        def isValid(word_a, word_b):
            for i in range(26):
                if word_a[i] == 1 == word_b[i]:
                    return False
            return True
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isValid(wordlist[i], wordlist[j]):
                    best = max(best, len(words[i]) * len(words[j]))
                    
        return best