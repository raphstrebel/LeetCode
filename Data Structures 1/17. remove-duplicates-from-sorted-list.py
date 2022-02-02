# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = set()
        
        if head is None:
            return None
        
        values = values.union({head.val})
        
        curr = head.next
        prev = head
        while curr:
            if curr.val in values:
                prev.next = curr.next
            else:
                prev = curr
                values = values.union({curr.val})
            curr = curr.next
        return head