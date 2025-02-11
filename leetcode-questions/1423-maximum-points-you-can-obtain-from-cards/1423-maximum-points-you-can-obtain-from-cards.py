class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        L = len(cardPoints)
        s, e = 0, L - k - 1
        ans = 0
        
        prefixSums = [cardPoints[0]]
        for i in range(1, L):
            prefixSums.append(prefixSums[i-1] + cardPoints[i])
        
        while e < L:
            ans = max(ans, prefixSums[-1] - (prefixSums[e] - (prefixSums[s-1] if s > 0 else 0)))
            s += 1
            e += 1
            
        return ans