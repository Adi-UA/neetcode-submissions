# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self,s,t):
        if not s and not t:
            return True
        if s and t and s.val==t.val:
            return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot and root:
            return True
        queue=deque()
        queue.append(root)
        while queue:
            len_q=len(queue)
            for _ in range(len_q):
                node=queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if self.isSame(node,subroot):
                    return True
        return False
