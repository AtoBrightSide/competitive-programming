class Node:
    def __init__(self):
        self.children = [None] *26
        self.end = False

class Trie:
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

    def search(self, word: str, isPrefix = False) -> bool:
        curr = self.root
        for ch in word:
            letter = ord(ch) - ord('a')
            if not curr.children[letter]:
                return False
            curr = curr.children[letter]
        return curr.end or isPrefix
            

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)