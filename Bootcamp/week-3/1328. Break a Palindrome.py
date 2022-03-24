class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        p = list(palindrome)
        s = set()
        for ch in palindrome:
            s.add(ch)
        if s == 1:
            if palindrome[0]=='a':
                p[-1] = 'b'
            else:
                p[0] = 'a'
            return "".join(p)
        for i in range(len(palindrome)):
            if p[i] != 'a':
                temp = p[i]
                p[i] = 'a'
                if p.count('a') == len(p):
                    p[i] = temp
                    p[-1]='b'
                return "".join(p)
        p[-1]='b'
        return "".join(p)
