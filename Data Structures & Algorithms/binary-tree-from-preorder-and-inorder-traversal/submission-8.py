# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap={val:idx for idx,val in enumerate(inorder)}
        self.pre_idx=0 # root value, moves up per layer
        def dfs(l,r): # l/r are bounds of inorder (inclusive)
            if l > r:
                return None
            rootVal=preorder[self.pre_idx]
            root=TreeNode(rootVal)
            mid=inorderMap[rootVal]
            self.pre_idx+=1 # for next layer
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        return dfs(0,len(preorder)-1)