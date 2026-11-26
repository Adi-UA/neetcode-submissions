# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque()
        q.append(root)
        while q:
            lenQ=len(q)
            sub=[]
            for _ in range(lenQ):
                root=q.popleft()
                q.append(root.left) if root.left else None
                q.append(root.right) if root.right else None
                sub.append(root.val)
            res.append(sub)
        return res
                
