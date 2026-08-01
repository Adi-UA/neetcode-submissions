# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def dfs(root):
            if not root:
                return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            print(left,right)
            print(abs(left)-abs(right))
            if abs(left - right) > 1:
                self.balanced=False
            return max(left,right)
        dfs(root)
        return self.balanced