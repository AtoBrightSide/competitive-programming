class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_2_take = [0] * numCourses
        graph = {}
        for course, preq in prerequisites:
            course_2_take[course] += 1
            if preq in graph:
                graph[preq].append(course)
            else:
                graph[preq] = [course]
        myQ = deque()
        for i in range(len(course_2_take)):
            if course_2_take[i] == 0:
                myQ.append(i)
        count = 0
        while myQ:
            curr = myQ.popleft()
            count += 1
            if curr in graph:
                for node in graph[curr]:
                    print(f"node -> {node}")
                    course_2_take[node] -= 1
                    if course_2_take[node] == 0:
                        myQ.append(node)
            
        return count == numCourses
