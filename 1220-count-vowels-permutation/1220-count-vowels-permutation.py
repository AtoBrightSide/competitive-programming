class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        @cache
        def dp(i, letter):
            if i == n:  return 1
            
            count = 0
            for l in rules[letter]:
                count += dp(i+1, l)
                
            return count
        
        possible_strings = 0
        for letter in "aeiou":
            possible_strings += dp(1, letter)
        
        return possible_strings % ((10 ** 9) + 7)