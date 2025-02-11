class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0] * n
        for frm, to in edges:
            incoming[to] += 1
        
        ans = [i for i in range(len(incoming)) if incoming[i] == 0]
        
        return ans