class Node:
    def __init__(self):
        self.children = [None] *26
        self.end = False
        
class TrieClass:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            letter = ord(ch) - ord('a')
            if not curr.children[letter]:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.end = True
    
    def startsWith(self, word):
        curr = self.root
        root = ""
        for ch in word:
            letter = ord(ch) - ord('a')
            if not curr.children[letter]:
                return word
            else:
                root += chr(letter + ord('a'))
                curr = curr.children[letter]
                if curr.end:
                    return root
            
        return word
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieClass()
        for word in dictionary:
            trie.insert(word)
        ans = ""
        sentence = sentence.split()
        for word in sentence:
            ans += " " + trie.startsWith(word)
                
        return ans[1:]