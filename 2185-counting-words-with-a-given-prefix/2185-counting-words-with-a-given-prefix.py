class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        L = len(pref)
        for i, word in enumerate(words):
            if L <= len(word) and pref == word[:L]:
                count += 1
        
        return count