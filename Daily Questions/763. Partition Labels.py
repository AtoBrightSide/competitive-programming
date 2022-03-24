class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = i

        ans, st, en = [], 0, freq[s[0]]
        for i in range(len(s)):
            if freq[s[i]] >= en:
                if i == freq[s[en]]:
                    ans.append(en - st + 1)
                    if i == len(s) - 1:
                        return ans
                    en = freq[s[i + 1]]
                    st = i + 1
                else:
                    en = freq[s[i]]
