class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        s, e = 0, len(cardPoints) - k - 1
        ans = 0
        
        prefixSums = [cardPoints[0]]
        for i in range(1, len(cardPoints)):
            prefixSums.append(prefixSums[i-1] + cardPoints[i])
        
        while e < len(cardPoints):
            ans = max(ans, total - (prefixSums[e] - (prefixSums[s-1] if s > 0 else 0)))
            s += 1
            e += 1
            
        return ans