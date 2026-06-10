# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        current=head # start iterating through linked list
        node1=ListNode(current.val) # get first value
        head_rev=node1 # initialize head of reversed linked list
        current=current.next # move down input linked list
        return Solution.create_reverseList(current,head_rev)

    def create_reverseList(current,tail):
        if not current:
            return tail
        else:
            head=ListNode(current.val)
            print(head.val,tail.val)
            head.next=tail
            current=current.next
            return Solution.create_reverseList(current,head)