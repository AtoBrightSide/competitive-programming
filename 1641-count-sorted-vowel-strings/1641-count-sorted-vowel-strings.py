class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        def dfs(index, curr):
            nonlocal count
            for i in range(index, len(vowels)):
                if len(curr) == n:
                    count += 1
                    return
                
                curr.append(vowels[i])
                dfs(i, curr)
                curr.pop()
            return
        
        dfs(0, [])
        return count