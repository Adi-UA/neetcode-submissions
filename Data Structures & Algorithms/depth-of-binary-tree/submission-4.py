from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        q=deque()
        q.append(root)
        length=0
        while q:
            len_q=len(q)
            for _ in range(len_q):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            length+=1
        return length