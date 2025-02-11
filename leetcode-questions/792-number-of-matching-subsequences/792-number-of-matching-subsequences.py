class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
    
    def search(self, word, s):
        curr = self.root
        temp = 0
        for i, ch in enumerate(word):
            if curr.children[ch].index == None:
                curr.children[ch].index = -1
                for j in range(temp, len(s)):
                    if ch == s[j]:
                        curr.children[ch].index = j
                        temp = j + 1
                        break
            
            if curr.children[ch].index < 0:    
                return False
            temp = curr.children[ch].index + 1
            curr = curr.children[ch]
        return True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        valid_subs = 0
        
        words.sort()
        for word in words:  
            trie.insert(word)
            
        for word in words:
            valid_subs += 1 if trie.search(word, s) else 0
        
        return valid_subs