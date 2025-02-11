class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeInMin = lambda time: (int(time[:2]) * 60) + int(time[3:])
        
        print(timePoints)
        timePoints = [timeInMin(timePoints[i]) for i in range(len(timePoints))]
        
        timePoints.sort()
        print(timePoints)
        minDiff = float('inf')
        for i in range(len(timePoints)):
            if (timePoints[i] >= 1080 or timePoints[i] <= 360) and (timePoints[i-1] >= 1080 or timePoints[i-1] <= 360):
                minDiff = min(minDiff, abs(1440 - max(timePoints[i], timePoints[i-1]) + min(timePoints[i], timePoints[i-1])))
            
            minDiff = min(minDiff, abs(timePoints[i] - timePoints[i-1]))
            
        return minDiff