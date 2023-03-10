# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.used = set()
        self.nodes = []

    def getRandom(self) -> int:
        if self.head not in self.used and self.head:
            self.used.add(self.head)
            pick = self.head
            self.nodes.append(pick.val)
            self.head = self.head.next
            return pick.val
        else:
            pick = int(random.random() * len(self.nodes))
            return self.nodes[int(pick)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()