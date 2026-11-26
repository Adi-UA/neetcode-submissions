class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle (s is midpoint rounded up)
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next
        prev=None
        curr=s
        # reverse list
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        # merge lists
        l2=prev
        l1=head
        while l2.next:
            nxt1,nxt2=l1.next,l2.next
            l1.next=l2
            l2.next=nxt1
            l1,l2=nxt1,nxt2
        