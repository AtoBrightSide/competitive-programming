class Solution:
    def bestClosingTime(self, customers: str) -> int:
        track_left = [0]
        for i in range(1, len(customers)):
            curr = 1 if customers[i - 1] == "N" else 0
            track_left.append(track_left[-1] + curr)
        track_left.append(track_left[-1])
        
        track_right = [1 if customers[-1] == "Y" else 0]
        for i in range(len(customers) - 2, -1, -1):
            curr = 1 if customers[i] == "Y" else 0
            track_right.append(track_right[-1] + curr)
        
        track_right = track_right[::-1]
        track_right.append(0)
        
        earliest_hour = len(customers)
        min_penalty = float("inf")
        for i in range(len(track_left)):
            penalty = track_right[i] + track_left[i]
            if penalty < min_penalty:
                earliest_hour = i
                min_penalty = penalty
        
        return earliest_hour