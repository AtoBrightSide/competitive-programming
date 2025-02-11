class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b:
            return "".join(['ab' for i in range(a)])
        
        flag = False
        answer = []
        
        while a >= 0 and b >= 0:
            if flag:
                curr = "ba" * a if answer[-1][-1] == 'a' else "ab" * a
                answer.append(curr)
                return "".join(answer)
            
            if a > b:
                if a > 1:
                    answer.append("aa")
                    a -= 2
                else:
                    answer.append("a")
                    a -= 1
                if b:   
                    answer.append('b')
                    b -= 1
                flag = a == b
            else:
                if b > 1:
                    answer.append("bb")
                    b -= 2
                else:
                    answer.append("b")
                    b -= 1
                if a:   
                    answer.append('a')
                    a -= 1
                flag = a == b
        
        