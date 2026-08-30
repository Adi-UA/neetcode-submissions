# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # go through nodes and store into seen hash set, if next one is already in seen, return False
        seen=set()
        curr=head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr=curr.next
        return False
            