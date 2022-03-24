class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #         res = []
        #         for i in range(len(citations)):
        #             res.append(min(citations[i], len(citations)-i))

        #         return max(res)
        best = -1
        l, r = 0, len(citations) - 1
        while l <= r:
            md = l + (r - l) // 2
            if citations[md] >= (len(citations) - md):
                best = max(best, len(citations) - md)
                r = md - 1
            else:
                l = md + 1
                best = max(best, citations[md])

        return best
