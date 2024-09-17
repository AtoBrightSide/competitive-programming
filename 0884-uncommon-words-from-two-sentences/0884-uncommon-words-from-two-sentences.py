class Solution:
    def helper(self, counter1, counter2):
        uncommon_words = []
        for word, freq in counter1.items():
            if freq == 1 and word not in counter2:
                uncommon_words.append(word)
        return uncommon_words
    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_counter_s1 = Counter(s1.split(" "))
        word_counter_s2 = Counter(s2.split(" "))
            
        return self.helper(word_counter_s1, word_counter_s2) + self.helper(word_counter_s2, word_counter_s1)
    
    