# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ = self.get_len(head)
        remove_elem = len_ - n
        new_head = head
        if remove_elem == 0:
            new_head = new_head.next
            return new_head
        i = 1
        new_curr = new_head
        while new_curr.next:
            if i == remove_elem:
                new_curr.next = new_curr.next.next
                return new_head
            new_curr = new_curr.next
            i += 1
        return new_head
    def get_len(self, head):
        len_ = 1
        curr = head
        while curr.next:
            len_ += 1
            curr = curr.next
        return len_