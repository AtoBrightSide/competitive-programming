class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr1 = ptr2 = 0
        longest = 0
        tracker = {}
        
        while ptr1 < len(s):
            while ptr2 < len(s) and s[ptr2] not in tracker:
                tracker[s[ptr2]] = 1
                ptr2 += 1
            
            longest = max(longest, len(tracker))
            if tracker[s[ptr1]] == 1:
                del tracker[s[ptr1]]
            
            ptr1 += 1
        
        return longest

# 2nd time trying
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow_pointer = 0
        longest = 0
        store = set()
        for letter in s:
            while letter in store:
                curr_letter = s[slow_pointer]
                store.remove(curr_letter)
                slow_pointer += 1
            store.add(letter)
            longest = max(longest, len(store))

        return longest
