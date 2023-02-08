class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        justified = []
        while i < len(words):
            count = 0
            curr_line = []
            while i < len(words) and count + len(words[i]) <= maxWidth:
                curr_line.append(words[i])
                count += len(words[i]) + 1
                i += 1
            temp = maxWidth - (count - 1)
            j = 0
            L = len(curr_line)
            while temp and L > 1:
                if (j % L) != L - 1:
                    curr_line[j % L] += " "
                    temp -= 1
                j += 1
                
            curr_line = " ".join(curr_line)
            curr_line += " " * abs(maxWidth - len(curr_line))
            justified.append(curr_line)
        
        last_line = " ".join(justified[-1].split())
        last_line += " " * abs(maxWidth - len(last_line))
        
        justified[-1] = last_line
        return justified