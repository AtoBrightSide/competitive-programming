class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            curr = log.split()
            if curr[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([" ".join(curr[1:]), curr[0] + " "])
        
        letter_logs.sort()
        final_order = []
        for content, ident in letter_logs:
            final_order.append(ident + content)
        
        final_order.extend(digit_logs)

        return final_order
        
        