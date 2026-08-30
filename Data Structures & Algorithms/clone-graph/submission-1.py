"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit=set()
        q=deque()
        q.append(node)
        mp={}
        while q:
            n = q.popleft()
            if n in visit:
                continue
            visit.add(n)
            if n.val not in mp:
                mp[n.val]=Node(val=n.val)
            nCopy=mp[n.val]
            for neighbor in n.neighbors: # add and create deepcopy of neighbors 
                # create neighbor if necessary
                if neighbor.val not in mp:
                    mp[neighbor.val]=Node(val=neighbor.val)
                # add to node copy as a neighbor copy
                nCopy.neighbors.append(mp[neighbor.val])
                # add to queue
                q.append(neighbor)
        return mp[node.val]