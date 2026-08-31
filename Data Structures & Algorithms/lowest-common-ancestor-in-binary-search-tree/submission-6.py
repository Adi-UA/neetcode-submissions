from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # keep going down, if curr value is between (inclusive), that's the LCA
        # works bc this is a BST

        # BFS
        queue=deque([root])
        while queue:
            n=queue.popleft()
            if q.val<=n.val<=p.val or p.val<=n.val<=q.val:
                return n
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        