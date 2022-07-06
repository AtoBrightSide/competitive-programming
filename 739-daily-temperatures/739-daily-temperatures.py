class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, curr = stack.pop()
                ans[curr] = i - curr
                
            stack.append([temp, i])
            
        return ans