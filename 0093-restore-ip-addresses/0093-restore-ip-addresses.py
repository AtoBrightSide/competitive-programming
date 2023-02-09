class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        is_valid = lambda segment: 0 <= int(segment) <= 255 and str(int(segment)) == segment

        def bt(s, segments, start, res):
            if start == len(s) and len(segments) == 4:
                res.append(".".join(segments))
                return
            if start >= len(s) or len(segments) >= 4:
                return
            for end in range(start, min(start + 3, len(s))):
                if is_valid(s[start:end + 1]):
                    bt(s, segments + [s[start:end + 1]], end + 1, res)

        ans = []
        bt(s, [], 0, ans)
        return ans