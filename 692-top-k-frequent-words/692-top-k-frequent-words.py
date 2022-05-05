class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = defaultdict(int)
        
class TrieClass:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.count[word] += 1
        
    def search(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.count[word]
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = TrieClass()
        
        for word in words:
            trie.insert(word)
        
        myDic = {}
        for word in words:
            myDic[word] = -trie.search(word)
            
        myHeap = [(val, key) for key, val in myDic.items()]
        heapq.heapify(myHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(myHeap)[1])
        return res