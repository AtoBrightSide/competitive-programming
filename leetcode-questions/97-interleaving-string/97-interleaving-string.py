class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 + s2 == s3 or s2 + s1 == s3:  return True
        memo, curr = {}, []
        def dp(i1, i2, i3):
            if i1 >= len(s1) and i2 >= len(s2):
                return curr == list(s3)
            
            if (i1, i2) in memo:    return memo[(i1, i2)]
            
            one = two = False
            if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                curr.append(s1[i1])
                one = dp(i1+1, i2, i3+1)
                curr.pop()
            
            if one: return True
            
            if i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                curr.append(s2[i2])
                two = dp(i1, i2+1, i3+1)
                curr.pop()
            
            memo[(i1, i2)] = one or two
            
            return memo[(i1, i2)]
        
        return dp(0, 0, 0)