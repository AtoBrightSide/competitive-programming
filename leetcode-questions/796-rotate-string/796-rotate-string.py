class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        
        if len(s) < 3:  return s[::-1] == goal or s == goal
        
        mySet = set()
        for i in range(len(s)-2):
            mySet.add(s[i:i+3])
        mySet.add(s[-2:] + s[0])
        mySet.add(s[-1:] + s[:2])
        
        mySet2 = set()
        for i in range(len(goal)-2):
            mySet2.add(goal[i:i+3])
        mySet2.add(goal[-2:] + goal[0])
        mySet2.add(goal[-1:] + goal[:2])
        
        return mySet2 == mySet