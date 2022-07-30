class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subs = set()
        sub_counter = defaultdict(int)
        for w in words2:
            curr = defaultdict(int)
            for ch in w:    
                subs.add(ch)
                curr[ch] += 1
            for ch in w:
                sub_counter[ch] = max(sub_counter[ch], curr[ch])
        
        words2 = list(subs)
        
        L = len(words2)
        universal = []
        for word in words1:
            if L <= len(word):
                word_counter = Counter(word)
                flag = True
                for ch in words2:
                    if ch not in word or word_counter[ch] < sub_counter[ch]:  
                        flag = False
                if flag:    
                    universal.append(word)
                
        return universal