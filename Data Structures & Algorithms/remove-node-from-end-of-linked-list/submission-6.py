class ListNode():
    def __init__(self,val=None,nxt=None):
        self.val=val
        self.next=nxt

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length:
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1
        # start with dummy (in case 0th node removed)
        # i tracks which node, and remove when on nth
        nFromLeft=length-n+1
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        i=0
        prev=None
        while i < nFromLeft:
            prev=curr
            curr=curr.next
            i+=1
        # now curr is at the node you want to remove
        nxt=curr.next
        prev.next=nxt
        return dummy.next