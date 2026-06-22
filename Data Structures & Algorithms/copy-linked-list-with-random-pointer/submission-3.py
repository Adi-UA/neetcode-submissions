"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        existing,new={},{}
        curr=head
        i=0
        # initialize map reference to existing nodes
        while curr:
            existing[curr]=[i]
            new[i]=Node(curr.val)
            curr=curr.next
            i+=1
        curr=head
        # add random index to existing map
        while curr:
            rand=curr.random
            rand_i=existing.get(rand,None)
            if rand_i:
                existing[curr].append(rand_i[0])
            else:
                existing[curr].append(None)
            curr=curr.next
        print(existing)
        print(new)
        # then create deep copy
        for k,(i,i_rand) in existing.items():
            print(i)
            if k.next:
                new[i].next=new[i+1]
            else:
                new[i].next=None
            if i_rand is None:
                new[i].random=None
            else:
                new[i].random=new[i_rand]
        return new[0]
