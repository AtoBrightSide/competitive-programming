# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        myStack = []
        while head:
            nums.append(head.val)
            head = head.next
        ans = [0]*len(nums)
        myStack.append([0, nums[0]])
        for i in range(len(nums)):
            while myStack and myStack[-1][1] < nums[i]:
                index, val = myStack.pop()
                ans[index] = nums[i]
            myStack.append([i, nums[i]])
            
        return ans