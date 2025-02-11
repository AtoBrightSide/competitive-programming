class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [[nums1[0] + nums2[0], 0, 0]]
        ans = []
        used = set((0, 0))
        for _ in range(k):
            if heap:
                _, i, j = heappop(heap)
                ans.append([nums1[i], nums2[j]])
            
            if j < len(nums2) - 1 and (i, j + 1) not in used:
                heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                used.add((i, j + 1))
            if i < len(nums1) - 1 and (i + 1, j) not in used:
                heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                used.add((i + 1, j))
            
        return ans