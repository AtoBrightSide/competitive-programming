class Solution:
    def hIndex(self, citations: List[int]) -> int:
        memo = defaultdict(int)
        def countOf(num):
            for c in citations:
                if c >= num:    memo[num] += 1
            
            return memo[num]
        
        for i in range(len(citations), -1, -1):
            if countOf(i) >= i:
                return i