class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        temp = [0] * 101
        for h in heights:
            temp[h] += 1
        expected = []
        for i, t in enumerate(temp):
            while t:
                expected.append(i)
                t -= 1
        
        ans = 0
        for i, h in enumerate(heights):
            if h != expected[i]:    ans += 1
        return ans