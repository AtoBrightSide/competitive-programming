class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        def bs(num):
            l,r = 0, len(prefix) - 1
            while l <= r:
                md = l + (r - l) // 2
                
                if prefix[md] == num:   return md
                if prefix[md] > num:    r = md - 1
                else:   l = md + 1
            
            return r
        
        answer = []
        for q in queries:   answer.append(bs(q) + 1)
        
        return answer
                