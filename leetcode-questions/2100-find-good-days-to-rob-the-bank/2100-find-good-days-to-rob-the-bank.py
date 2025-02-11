class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        count = [[1 for _ in range(2)] for _ in range(len(security))]
        L = len(security) - 1
        
        for i in range(len(security)):
            if i > 0 and security[i] <= security[i-1]:
                count[i][0] += count[i-1][0]
            if L-i < L and security[L - i] <= security[L - i + 1]:
                count[L - i][1] += count[L - i + 1][1]
        
        goodDays = []
        for i, val in enumerate(count):
            l, r = val
            if l >= time + 1 <= r:
                goodDays.append(i)
        
        return goodDays