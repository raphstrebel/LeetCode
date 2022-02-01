# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        i = 0
        while fast:
            if fast.next == slow.next:
                return True
            fast = fast.next
            if i == 1:
                slow = slow.next
                i = 0
            else:
                i = 1
        return False