class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        for word in words:
            curr = []
            for ch in word:
                index = ord(ch) - ord("a")
                curr.append(morse[index])
            transformations.add("".join(curr))
        
        return len(transformations)