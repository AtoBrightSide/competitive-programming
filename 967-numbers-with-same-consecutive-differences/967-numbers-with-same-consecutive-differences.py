class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:  return [int(str(i) * n) for i in range(1,10)]
        
        answer = []
        def count(num):
            if len(num) == n:
                answer.append(int(num))
                return
            
            for i in range(0, 10):
                if abs(int(num[-1]) - i) == k:
                    num += str(i)
                    count(num)
                    num = num[:-1]
                    
        
        for i in range(1, 10):  count(str(i))
        
        return answer