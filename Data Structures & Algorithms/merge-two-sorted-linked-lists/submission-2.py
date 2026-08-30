# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=list1,list2
        dummy=ListNode()
        curr=dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                print("curr1 less")
                curr.next=curr1
                curr1=curr1.next
            else:
                print("curr2 less")
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next
        if curr1:
            curr.next=curr1
        else:
            curr.next=curr2
        return dummy.next