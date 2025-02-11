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

# Another try
class Solution:
    def __init__(self):
        self.longest = 1
        self.ans = [0,0]

    def checkPalindrome(self, left, right, s):
        while left > -1 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > self.longest:
                self.longest = right - left + 1
                self.ans = [left, right]
            left -= 1
            right += 1

    def longestPalindrome(self, s: str) -> str:
        for index, letter in enumerate(s):
            # for odd
            self.checkPalindrome(index - 1, index + 1, s)

            # for even
            self.checkPalindrome(index, index + 1, s)

        start, end = self.ans
        return s[start : end + 1]
