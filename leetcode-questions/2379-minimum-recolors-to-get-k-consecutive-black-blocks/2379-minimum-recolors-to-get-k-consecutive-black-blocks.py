class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        best = float("inf")
        for i in range(len(blocks)):
            count = ops = 0
            for j in range(i, len(blocks)):
                if blocks[j] == "W":
                    ops += 1
                count += 1
                if count == k:
                    best = min(best, ops)
        
        return best