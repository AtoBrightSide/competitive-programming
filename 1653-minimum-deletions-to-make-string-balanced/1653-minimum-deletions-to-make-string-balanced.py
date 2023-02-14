class Solution:
    def dp(self, index, letter, s, memo):
        state = (index, letter)
       
        if state not in memo:
            if letter == 'b':
                memo[state] = self.dp(index+1, letter, s, memo) + int(s[index] == 'a')
            else:
                # print(index)
                if s[index] == 'b':
                    memo[state] = min(self.dp(index+1, 'b', s, memo), self.dp(index+1, 'a', s, memo)+1)
                else:
                    memo[state] = self.dp(index+1, 'a', s, memo)
        return memo[state]
    def minimumDeletions(self, s: str) -> int:
        memo = {(len(s),'a') : 0, (len(s),'b'):0}
        return min(self.dp(0, 'a', s ,memo), self.dp(0, 'b', s, memo))