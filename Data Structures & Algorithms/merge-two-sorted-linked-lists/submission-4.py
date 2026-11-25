class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        cur1,cur2=list1,list2
        dummy=ListNode()
        merged=dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                merged.next=cur1
                cur1=cur1.next
            else:
                merged.next=cur2
                cur2=cur2.next
            merged=merged.next
        if cur1:
            merged.next=cur1
        if cur2:
            merged.next=cur2
        return dummy.next
        