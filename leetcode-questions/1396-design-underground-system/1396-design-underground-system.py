class UndergroundSystem:

    def __init__(self):
        self.info = {}
        self.route = {}
        self.routeCount = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.info[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInPlace, checkInTime = self.info[id]
        if (checkInPlace, stationName) not in self.route:
            self.route[checkInPlace, stationName] = t - checkInTime
            self.routeCount[(checkInPlace, stationName)] = 1
        else:
            self.route[checkInPlace, stationName] += t - checkInTime
            self.routeCount[(checkInPlace, stationName)] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.route[startStation, endStation] / self.routeCount[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)