# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        fast = head
        
        i = 0
        while fast.next is not None:
            fast = fast.next
            if i == 0:
                curr = curr.next
                i += 1
            else:
                i -= 1
        return curr