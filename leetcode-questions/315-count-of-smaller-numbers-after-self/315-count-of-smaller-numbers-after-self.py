from collections import deque
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = SortedList()
        answer = deque([])
        for num in reversed(nums):
            answer.appendleft(count.bisect_left(num))
            count.add(num)
            
        return answer