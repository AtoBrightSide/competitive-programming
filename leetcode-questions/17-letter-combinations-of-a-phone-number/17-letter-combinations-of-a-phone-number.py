class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        
        def dfs(index, curr):
            for letter in combos[str(digits[index])]:
                curr.append(letter)
                nxt = index + 1
                if nxt < len(digits):
                    dfs(nxt, curr)
                else:
                    res.append("".join(curr))
                curr.pop()
        
        if not digits == "":
            dfs(0, [])
                        
        return res