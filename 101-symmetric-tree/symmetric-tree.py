# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None: # base case
            return True
        if p==None or q==None or p.val!=q.val: #base case
            return False
        return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left) #recursive

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left,root.right)