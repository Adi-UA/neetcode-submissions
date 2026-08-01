from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            node_p, node_q = queue.popleft()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
        return True