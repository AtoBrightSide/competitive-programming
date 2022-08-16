class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = Trie()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Trie()
            curr = curr.children[index]
        curr.isEnd = True
    
    def longestWord(self, words: List[str]) -> str:
        for w in words: self.insert(w)
            
        def traverseTrie(node):
            if not node.isEnd:  return ""
            word = ""
            for i, ch in enumerate(node.children):
                if ch and ch.isEnd:
                    temp = chr(i + ord('a')) + traverseTrie(ch)
                    word = temp if len(word) < len(temp) else word
            return word
        
        answer = ""
        for i, node in enumerate(self.root.children):
            if node and node.isEnd:
                curr = chr(i + ord('a')) + traverseTrie(node)
                answer = curr if len(curr) > len(answer) else answer
        return answer