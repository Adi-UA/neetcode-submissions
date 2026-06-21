# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        curr,i=prev,1
        prev=None
        while curr:
            nxt=curr.next
            # if list is len1
            print(f"i: {i}")
            if i==n:
                # in case nothing after, just end
                if not nxt:
                    return prev
                else:
                    # save off next2
                    nxt2=nxt.next
                    # update nxt pointer to prev
                    nxt.next=prev
                    # update curr and prev to move up (prev no longer curr)
                    prev=nxt
                    curr=nxt2
            else:
                curr.next=prev
                prev=curr
                curr=nxt
            i+=1
        return prev