class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        outgoing = defaultdict(list)
        
        for c, p in prerequisites:
            indegrees[p] += 1
            outgoing[c].append(p)
            
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:    queue.append(i)

        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            for c in outgoing[curr]:
                indegrees[c] -= 1
                if indegrees[c] == 0:   queue.append(c)
        
        return count == numCourses