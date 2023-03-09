class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        L = sum(cookies)
        def backtrack(i, kids):
            if i >= len(cookies):
                return max(kids)
            
            fair = L
            for idx in range(len(kids)):
                kids[idx] += cookies[i]
                if kids[idx] < fair:
                    fair = min(fair, backtrack(i + 1, kids))
                kids[idx] -= cookies[i]
            
            return fair
        
        return backtrack(0, [0 for _ in range(k)])