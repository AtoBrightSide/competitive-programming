class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        answer, plates, candles = [], [], []
        count = 0
        for i, ch in enumerate(s):
            if ch == "|":   candles.append(i)
            count += 1 if ch == "*" else 0
            plates.append(count)
        
        def bs(i, flag):
            l, r = 0, len(candles) - 1
            best = -1
            while l <= r:
                md = l + (r - l) // 2
                
                if candles[md] == i: return md
                if i < candles[md]: 
                    if flag:   best = md
                    r = md - 1
                else:  
                    if not flag:   best = md
                    l = md + 1
            return best
        
        for s, e in queries:
            start, end = bs(s, True), bs(e, False)
            if start>-1 and end>-1 and start < end + 1:
                answer.append(plates[candles[end]] - plates[candles[start]])
            else:
                answer.append(0)
        return answer