class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        sub_counter = defaultdict(int)
        for w in words2:
            curr = defaultdict(int)
            for ch in w:    
                curr[ch] += 1
                sub_counter[ch] = max(sub_counter[ch], curr[ch])
        
        words1 = set(words1)
        
        universal = []
        for word in words1:
            word_counter = Counter(word)
            flag = True
            for ch, count in sub_counter.items():
                if ch not in word or word_counter[ch] < count:  
                    flag = False

            if flag:        universal.append(word)
                
        return universal