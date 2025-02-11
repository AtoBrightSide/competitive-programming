class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {
            'a': ['i', 'e', 'u'],
            'e': ['a','i'],
            'i': ['e', 'o'],
            'o': ['i'],
            'u': ['o','i'],
        }
        mapper = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4,
        }
        dp = [[0] * 5 for i in range(n)]
        dp[0] = [1] * 5
        
        for row in range(1, n):
            for i, val in enumerate("aeiou"):
                for letter in rules[val]:
                    dp[row][i] += dp[row - 1][mapper[letter]]
        
        return sum(dp[-1]) % ((10 ** 9) + 7)