class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for ch in magazine:
            letters[ch] += 1
        for ch in ransomNote:
            if letters[ch] == 0:   return False
            letters[ch] -= 1
        return True