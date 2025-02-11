class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word) > len(sequence):   return 0
        
        ans = 0
        for i in range(len(sequence)):
            r = i
            while r < len(sequence):
                l = 0
                while r < len(sequence) and sequence[r] == word[l % len(word)]:
                    l += 1
                    r += 1
                if l >= len(word):
                    ans = max(ans, l // len(word))
                r += 1
        
        return ans