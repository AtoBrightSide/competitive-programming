class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for startDate, endDate in self.calendar:
            if startDate <= start < endDate or startDate < end < endDate:   return False
            if start <= startDate < end or start < endDate < end:   return False
        
        self.calendar.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)