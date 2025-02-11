class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or sorted(s) != sorted(goal): return False
        
        count = 0
        for i in range(len(s)):
            if s[i] != goal[i]: count += 1
        
        if count == 2:  return True
        elif count == 1 or count > 2:    return False
        elif s == goal:
            s_counter = Counter(s)
            for ch, freq in s_counter.items():
                if freq != 1:   return True
        
        return False
            
        
        