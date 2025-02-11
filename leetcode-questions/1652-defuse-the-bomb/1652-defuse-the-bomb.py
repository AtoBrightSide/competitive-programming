class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        prefix = [code[0]]
        suffix = [code[-1] for _ in range(N)]
        for i in range(1, len(code)):
            prefix.append(prefix[-1] + code[i])
            suffix[N-1-i] = suffix[N-i] + code[N-1-i]
        
        for i in range(len(code)):
            temp = abs(k)
            if k < 0: 
                if i - temp >= 0:
                    code[i] = suffix[i-temp] - suffix[i]
                else:
                    code[i] = suffix[i-temp] + (prefix[i-1] if i > 0 else 0)
            if k > 0:
                if (i + k) < N:  
                    code[i] = prefix[i+temp] - prefix[i]
                else:   
                    code[i] = prefix[(i+temp)%N] - prefix[i] + prefix[-1]
            
            if k == 0:  code[i] = 0
        
        return code