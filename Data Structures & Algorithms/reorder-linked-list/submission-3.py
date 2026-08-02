# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes={}
        curr=head
        i=0
        while curr:
            nodes[i]=curr
            i+=1
            curr=curr.next
        finalOrder=[]
        i=0
        while len(finalOrder)<len(nodes):
            if len(finalOrder)%2==0:
                finalOrder.append(i)
                i+=1
            else:
                finalOrder.append(len(nodes)-i)

        dummy=ListNode()
        curr=dummy
        for i in finalOrder:
            curr.next=nodes[i]
            curr=curr.next
        curr.next=None