# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global stack, res
        stack=[]
        res=[]
        def check(root):
            if not root:
                if stack:
                    res.append(stack.pop().val)
            else:
                stack.append(root)
                check(root.left)
                check(root.right)
        check(root)
        print(res)

        for i in range(1,len(res)):
            if res[i-1]>=res[i]:
                return False
        return True

        