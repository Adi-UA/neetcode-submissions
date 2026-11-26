# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method 1 - 2 pass: 1) find N 2) remove N-nth position
        # method 2 - two pointers that are n apart
        dummy=ListNode()
        dummy.next=head
        prev,r=dummy,head
        steps=1
        while steps<n:
            r=r.next
            steps+=1
        while r.next:
            prev=prev.next
            r=r.next
        prev.next=prev.next.next
        return dummy.next

        

        
        