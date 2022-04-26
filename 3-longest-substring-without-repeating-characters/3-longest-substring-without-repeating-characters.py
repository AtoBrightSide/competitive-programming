class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = fast = 0
        best = 0
        tracker = defaultdict(int)
        
        '''
        k:1
        e:1
        
        '''
        
        while slow < len(s):
            while fast<len(s) and s[fast] not in tracker:
                tracker[s[fast]] += 1
                fast += 1
                
            best = max(best, len(tracker))
            while slow<=fast<len(s) and s[slow] != s[fast]:
                del tracker[s[slow]]
                slow += 1
                
            del tracker[s[slow]]
            slow += 1
        return best