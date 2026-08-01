# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            layer=[]
            len_queue=len(queue)
            for _ in range(len_queue):
                node=queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if layer:
                    res.append(layer)
        return res

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []

    #     q = [[root]]
    #     while True:
    #         next_layer = []
    #         for node in q[-1]:
    #             if node.left:
    #                 next_layer.append(node.left)
    #             if node.right:
    #                 next_layer.append(node.right)
    #         if not next_layer:
    #             break
    #         q.append(next_layer)

    #     return [[node.val for node in layer] for layer in q]