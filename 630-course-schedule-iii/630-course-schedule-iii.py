class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda d: d[1])
        heap = []
        total_days = 0
        i = 0
        ans = 0
        max_ans = 0
        while i < len(courses):
            course = courses[i]
            if total_days + course[0] <= course[1]:
                heapq.heappush(heap, -course[0])
                total_days += course[0]
                i += 1
                ans += 1
            else:
                if heap and -heap[0] > course[0]:
                    total_days = total_days + heapq.heappop(heap)
                    ans -= 1
                else:
                    i += 1
            max_ans = max(max_ans, ans)
        return max_ans