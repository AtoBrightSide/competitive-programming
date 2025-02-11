class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while sandwiches and students:
            if count == len(sandwiches):    return len(students)
            count += 1
            
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:   students.append(students.popleft())
        
        return 0