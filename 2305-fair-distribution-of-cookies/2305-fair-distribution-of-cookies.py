class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        unfair = sum(cookies)
        def backtrack(i, kids):
            nonlocal unfair
            if i >= len(cookies):
                unfair = min(unfair, max(kids))
                return 
            
            for idx in range(len(kids)):
                kids[idx] += cookies[i]
                backtrack(i + 1, kids)
                kids[idx] -= cookies[i]
            
        backtrack(0, [0 for _ in range(k)])
        return unfair