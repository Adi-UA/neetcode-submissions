# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        node_map={}
        i=0
        # make node map
        while curr:
            node_map[i]=curr
            i+=1
            curr=curr.next
        # make new ordering list
        reorder=[]
        for i in range(len(node_map)):
            if i%2==0:
                reorder.append(int(i/2))
            else:
                reorder.append(int(len(node_map)-(i+1)/2))
        # start reordering
        print(reorder)
        print(node_map)
        r=0
        while r < len(reorder):
            i=reorder[r]
            curr=node_map[i]
            print(r)
            if r<len(reorder)-1:
                curr.next=node_map.get(reorder[r+1],None)
            else:
                curr.next=None
            r+=1
        return