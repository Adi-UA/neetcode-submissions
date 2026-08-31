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

        # Traverse down based on BST direction
        n=root
        while True:
            if n.val > p.val and n.val > q.val:
                # move left
                n=n.left
            elif n.val < p.val and n.val < q.val:
                # move right
                n=n.right
            else:
                return n

        