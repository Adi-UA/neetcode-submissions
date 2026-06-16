# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        l2=s.next # start from l2
        prev=None
        s.next=None # break link from l1->l2
        while l2:
            next=l2.next
            l2.next=prev
            prev=l2
            l2=next
        l1,l2=head,prev
        while l2:
            next1,next2=l1.next,l2.next
            l1.next=l2
            l2.next=next1
            l1,l2=next1,next2
        return
        