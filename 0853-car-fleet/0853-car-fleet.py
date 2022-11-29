class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], (target - position[i]) / speed[i]] for i in range(len(position))]
        cars.sort()
        
        i = 1
        fleets = [cars[0][1]]
        while i < len(cars):
            curr_car = cars[i][1]
            while fleets and fleets[-1] <= curr_car:
                fleets.pop()
            
            if i < len(cars):
                fleets.append(curr_car)
            i += 1
        
        return len(fleets)
            