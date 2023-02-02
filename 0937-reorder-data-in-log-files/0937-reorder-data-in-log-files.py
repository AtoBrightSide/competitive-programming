class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            curr_log = log.split(' ')
            
            if curr_log[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        srtltr = sorted(letters, key=lambda ch: (ch.split()[1:], ch.split()[0]))
        
        return srtltr + digits                