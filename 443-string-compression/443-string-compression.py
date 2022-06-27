class Solution:
    def compress(self, chars: List[str]) -> int:
        left, curr, right = 0, 1, 1
        
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            
            if right - left > 1:
                for ch in str(right - left):
                    chars[curr] = ch
                    curr += 1
            if right < len(chars):
                chars[curr] = chars[right]
                curr += 1
                left = right
                right += 1
            
        return curr