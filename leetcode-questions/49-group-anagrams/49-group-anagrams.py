class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for word in strs:
            curr = "".join(sorted(word))
            myDict[curr].append(word)
        res = []
        for key, val in myDict.items():
            res.append(val)
        
        return res