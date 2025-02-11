class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        times, ops = [60, 15, 5, 1], 0
        
        current_time = 60 * int(current[0:2]) + int(current[3:5])
        correct_time = 60 * int(correct[0:2]) + int(correct[3:5])
        diff = correct_time - current_time
        
        for time in times:
            ops += diff//time
            diff %= time
            
        return ops