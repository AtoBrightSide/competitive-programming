class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.comp(s) == self.comp(t)
                
    def comp(self, s):
        myS = []
        for i in range(len(s)):
            if myS and s[i] == "#":
                myS.pop()
                    
            if s[i] != "#":
                myS.append(s[i])
        return myS
    