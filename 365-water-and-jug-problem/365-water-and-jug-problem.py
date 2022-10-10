class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        done = set()
        def tryThis(curr_sum):
            if 0 > curr_sum or curr_sum > jug1Capacity + jug2Capacity:
                return False
            if curr_sum in done:
                return False
            if curr_sum == targetCapacity:
                return True
            
            done.add(curr_sum)
            this_one = tryThis(curr_sum + jug1Capacity) or tryThis(curr_sum + jug2Capacity)
            or_this = tryThis(curr_sum - jug1Capacity) or tryThis(curr_sum - jug2Capacity)
            
            return this_one or or_this
        
        return tryThis(0)