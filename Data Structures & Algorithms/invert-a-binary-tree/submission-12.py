# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # at every node, save left as tmp and reverse right and left
        # recursion or bfs both work
        
        # # BFS
        # if not root:
        #     return None
        # q=deque()
        # q.append(root)
        # while q:
        #     n=q.popleft()
        #     tmp=n.left
        #     n.left=n.right
        #     n.right=tmp
        #     if n.left:
        #         q.append(n.left)
        #     if n.right:
        #         q.append(n.right)
        # return root
    
        # DFS
        if not root:
            return None
        tmp=root.left
        root.left=root.right
        root.right=tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    