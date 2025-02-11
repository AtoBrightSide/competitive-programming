class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        for num, freq in count.items():
            if (freq / len(arr)) > (1 / 4):
                return num