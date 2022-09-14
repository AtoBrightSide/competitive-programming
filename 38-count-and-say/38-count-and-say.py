class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(nums, i):
            if i == 1:  return nums
            
            res = []
            for num in nums:
                if res and num == res[-1][0]:   res[-1][1] += 1
                else:   res.append([num,1])

            ans = []
            for num, times in res:  ans.append(str(times) + num)
            
            return recur("".join(ans), i - 1)
        
        return recur("1", n)