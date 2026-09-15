# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head # should this be head.next?
        while f and f.next:
            f=f.next.next
            s=s.next
        l2=s.next
        prev=None
        s.next=None
        while l2:
            nxt=l2.next
            l2.next=prev
            prev=l2
            l2=nxt
        l2 = prev
        l1 = head
        curr=l1
        while l2:
            l1nxt,l2nxt=l1.next,l2.next
            l1.next=l2
            l2.next=l1nxt
            l1,l2=l1nxt,l2nxt
