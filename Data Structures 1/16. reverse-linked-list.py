# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        prev = None
        while curr:
            new_head = ListNode(curr.val, next=prev)
            prev = new_head
            curr = curr.next
        return new_head