# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,low,high):
            if not node:
                return True
            if low >= node.val or high <= node.val:
                return False
            return (isValid(node.left,low,node.val) and isValid(node.right,node.val,high))
        return isValid(root,float("-infinity"),float("infinity"))
        

        