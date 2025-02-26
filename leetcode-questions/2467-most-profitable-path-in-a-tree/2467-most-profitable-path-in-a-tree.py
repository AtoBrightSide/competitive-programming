class Solution:
    def __init__(self):
        self.graph = {}
        self.amount = []
        self.bob_path = []

    def buildGraph(self, edges):
        for a, b in edges:
            if b not in self.graph:
                self.graph[b] = []
            if a not in self.graph:
                self.graph[a] = []

            self.graph[b].append(a)
            self.graph[a].append(b)

    def findPathToRoot(self, node, seen):
        self.bob_path.append(node)
        seen.add(node)

        if node == 0:
            return True

        for adjacent_node in self.graph[node]:
            if adjacent_node not in seen and self.findPathToRoot(adjacent_node, seen):
                return True

        seen.remove(node)
        self.bob_path.pop()
        return False

    def traverse(self, node, time, seen):
        # if reached a leaf node, return
        if len(self.graph[node]) == 1 and node != 0:
            # this would mean bob got to this node first
            if node not in self.tracker or (
                node in self.tracker and self.tracker[node] > time
            ):
                return self.amount[node]
            elif self.tracker[node] == time:
                return self.amount[node] / 2
            return 0

        curr_income = 0
        if node not in self.tracker or (
            node in self.tracker and self.tracker[node] > time
        ):
            curr_income = self.amount[node]
        elif self.tracker[node] == time:
            curr_income = int(self.amount[node] / 2)

        seen.add(node)
        max_income = -float("inf")
        for neighbor in self.graph[node]:
            if neighbor not in seen:
                max_income = max(max_income, self.traverse(
                    neighbor, time + 1, seen))
        seen.remove(node)

        return max_income + curr_income

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.amount = amount
        self.buildGraph(edges)

        if self.findPathToRoot(bob, set()):
            self.tracker = {node: time for time,
                            node in enumerate(self.bob_path)}

        return self.traverse(0, 0, set())
