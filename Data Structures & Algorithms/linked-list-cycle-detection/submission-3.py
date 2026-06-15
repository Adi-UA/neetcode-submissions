# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s=head
        f=head.next
        while s!=f:
            s=s.next
            if not f:
                return False
            f=f.next
            if not f:
                return False
            f=f.next
                
        return True
        