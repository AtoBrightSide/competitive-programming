class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque([])
        for i, num in enumerate(arr):
            if num == 0:
                queue.append(0)
            
            queue.append(num)
            if queue:
                arr[i] = queue.popleft()