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
        mp={}
        def dfs(node):
            if node.val not in mp:
                mp[node.val]=Node(val=node.val)
            nodeCopy=mp[node.val]
            if node in visit:
                return nodeCopy
            visit.add(node)
            for neighbor in node.neighbors:
                nodeCopy.neighbors.append(dfs(neighbor))
            return nodeCopy
        return dfs(node)