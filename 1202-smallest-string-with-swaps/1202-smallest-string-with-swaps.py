class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        rank = [1 for i in range(len(s))]
        
        def find(node):
            # nonlocal parent
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
            
        def unite(x, y):
            # nonlocal rank
            
            px = find(x)
            py = find(y)
            
            if px != py:
                if rank[px] >= rank[py]:
                    parent[py] = px
                    rank[px] += rank[py]
                    rank[py] = 0
                else:
                    parent[px] = py
                    rank[py] += rank[px]
                    rank[px] = 0
                    
        myDict = defaultdict(list)
        for x,y in pairs:
            unite(x,y)
        
        print(parent)
        for i in range(len(parent)):
            myDict[find(parent[i])].append(i)
        
        res = [0]*len(s)
        
        for key in myDict.keys():
            chars = [s[i] for i in myDict[key]]
            chars.sort()
            for i in range(len(chars)):
                res[myDict[key][i]] = chars[i]
                
        return "".join(res)
    