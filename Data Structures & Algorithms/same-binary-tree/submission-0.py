# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p,stack_q=[p],[q]
        same=True
        i=0
        while stack_p and stack_q:
            # make sure same length
            if len(stack_q) != len(stack_p):
                same=False
                break
            # bfs
            for _ in range(len(stack_p)):
                print(f"length of stack_p: {len(stack_p)}")
                print(f"stacks: {stack_p},{stack_q}")
                # compare values
                node_p=stack_p.pop()
                node_q=stack_q.pop()
                if (node_p is None) != (node_q is None): # if only one is none, break
                    same=False
                    break
                if not node_p:
                    continue
                if node_p.val != node_q.val:
                    same=False
                    break
                # update stack with children
                print(f"i: {i}");i+=1
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
        return same

