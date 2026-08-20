# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Attempt 3.5: O(N); iterative DFS checks in strictly ascending order of a true BST. Check if this tree is NOT strictly increasing, then return False if fails condition.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack,prev=[],float("-infinity")
        curr=root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                node=stack.pop()
                print(node.val)
                if node.val <= prev:
                    return False
                prev=node.val
                curr=node.right
        return True
        