class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent, rank, names = {}, {}, {}
        for account in accounts:
            for i in range(1,len(account)):
                parent[account[i]] = account[i]
                rank[account[i]] = 1
                names[account[i]] = account[0]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            pa = find(a) 
            pb = find(b)
            if pa != pb:
                if rank[pa] >= rank[pb]:
                    parent[pb] = pa
                    rank[pa] += rank[pb]
                    rank[pb] = 0
                else:
                    parent[pa] = pb
                    rank[pb] += rank[pa]
                    rank[pa] = 0
            
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                union(accounts[i][j], accounts[i][j+1])
        
        emails = defaultdict(list)
        for key, value in parent.items():
            emails[find(value)].append(key)
        
        res = []
        for name, email in emails.items():
            email.sort()
            res.append([names[name]] + email)
        
        return res