class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        odds = []
        for node, neigh in graph.items():
            L = len(neigh)
            if L % 2 and L == n - 1:
                return False
            if L % 2 and L != n - 1:
                odds.append([node, neigh])
        
        L = len(odds)
        if (L not in set([0, 2, 4])):
            return False
        if L == 0:
            return True
        
        def check(connect):
            for i in range(L):
                node, neigh = odds[i]
                # join node with c, d, or e
                for j in range(L):
                    if i != j and node not in odds[j][1] and not connect[i] and not connect[j]:
                        connect[i], connect[j] = True, True
                        if check(connect):  return True
                        connect[i], connect[j] = False, False

            return False not in connect
        
        if L == 2:
            for node in range(1, n + 1):
                if node not in odds[0][1] and node not in odds[1][1]:
                    return True
            return False
        return check([False] * L)