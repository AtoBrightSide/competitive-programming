class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > 1:  return num