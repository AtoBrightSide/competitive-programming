class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = curr = 0
        best, ans = 1, s[0]            
        valid = lambda x: 0 <= x < len(s)
        
        while curr < len(s):
            left = curr - 1
            
            if curr < len(s) - 1 and s[curr] == s[curr + 1]:
                if best < 2:
                    ans = s[curr:curr+2]
                    best = 2
                right = curr + 2
                while valid(left) and valid(right) and s[left] == s[right] and left != right:
                    if right - left + 1 > best:
                        ans = s[left:right+1]
                        best = max(best, right - left + 1)
                    left -= 1
                    right += 1
            left = curr - 1
            odd = curr + 1
            while valid(left) and valid(odd) and s[left] == s[odd] and left != odd:
                if odd - left + 1 > best:
                    ans = s[left:odd+1]
                    print(ans)
                    best = max(best, odd - left + 1)
                left -= 1
                odd += 1
            
            curr += 1
            
        return ans