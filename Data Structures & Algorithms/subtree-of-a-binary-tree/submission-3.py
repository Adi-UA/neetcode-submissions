# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self,p,q):
        # use dfs and traverse both trees
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val !=q.val:
            return False
        # o.w. check values
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursively check root to see if is sametree
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)