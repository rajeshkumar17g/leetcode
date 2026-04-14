# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen=[]
        def inorder(root):
            if root==None:
                return False
            left=inorder(root.left)
            if k-root.val in self.seen:
                return True
            self.seen.append(root.val)
            right=inorder(root.right)
            return left or right
        #---------------------------------
        res=[]
        return inorder(root)
        