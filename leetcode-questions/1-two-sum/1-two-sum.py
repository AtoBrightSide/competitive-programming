class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(list)
        for j, num in enumerate(nums):
            temp[num].append(j)

        for i, num in enumerate(nums):
            curr = target - num
            if curr in temp:
                if len(temp[curr]) > 1 and curr == num:
                    return temp[curr][:2]
                if curr != num:
                    return [temp[curr][0], temp[num][0]]