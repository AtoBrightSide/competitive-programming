class Solution:
    def convertToString(self, num, N):
        num = bin(num)[2:]
        while len(num) < N:
            num = "0" + num
            
        return num

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        all_strings = set([num for num in nums])

        for num in range(2**N):
            num = self.convertToString(num, N)
            if num not in all_strings:
                return num