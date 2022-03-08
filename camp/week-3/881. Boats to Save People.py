class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start, end = 0, len(people)-1
        boat_count = 0
        people.sort()
        while start <= end:
            if people[start] + people[end] > limit:
                end -= 1
                boat_count += 1
            elif people[start] + people[end] <= limit:
                start += 1
                end -= 1
                boat_count += 1
        return boat_count
