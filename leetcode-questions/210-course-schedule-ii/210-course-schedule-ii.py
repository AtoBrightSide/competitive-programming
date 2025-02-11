class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course2take = [0] * numCourses
        graph = defaultdict(set)
        for crs, preq in prerequisites:
            course2take[crs] += 1
            if preq in graph:
                graph[preq].append(crs)
            else:
                graph[preq] = [crs]
        myq = deque()
        for i in range(len(course2take)):
            if course2take[i] == 0:
                myq.append(i)
        tp = []
        while myq:
            curr = myq.popleft()
            tp.append(curr)
            for node in graph[curr]:
                course2take[node] -= 1
                if course2take[node] == 0:
                    myq.append(node)
        
        for course in course2take:
            if course == 1:
                return []
        
        return tp
        