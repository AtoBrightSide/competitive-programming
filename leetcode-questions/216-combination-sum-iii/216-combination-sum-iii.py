class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []        
    
        def dfs(index, curr):
            for i in range(index+1,10):
                curr.append(i)
                if len(curr) <= k:
                    dfs(i, curr)    
                if sum(curr) == n and len(curr) == k:
                    ans.append([x for x in curr])
                    curr.pop()
                    break
                curr.pop()

        dfs(0, [])
        
        return ans