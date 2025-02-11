class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [ch for ch in str(num)]
        max_num = -1
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                max_num = max(max_num, int("".join(num)))
                num[i], num[j] = num[j], num[i]
        
        return max(max_num, int("".join(num)))