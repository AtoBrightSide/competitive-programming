class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        count = 0
        def recur(i):
            nonlocal count
            if i == 1:  return count
            
            curr = math.ceil(math.log2(i))
            count += 1
            recur(i - (pow(2,curr) / 2))

            return
        
        recur(k)
        
        return 1 if count % 2 != 0 else 0