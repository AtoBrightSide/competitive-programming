class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = deque([])
        k %= len(nums)
        c = len(nums) - k
        
        for i, num in enumerate(nums):
            if i < c:   temp.append(num)
        
        p1, p2 = 0, c
        while p1 < len(nums):
            if p2 < len(nums):
                nums[p1] = nums[p2]
                p2 += 1
            else:
                nums[p1] = temp.popleft()
            p1 += 1