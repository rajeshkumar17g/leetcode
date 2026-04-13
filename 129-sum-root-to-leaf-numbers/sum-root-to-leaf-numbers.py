# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def helper(root,sum):
            if root==None:
                return ""
            
            if root.left==None and root.right==None:
                self.total+=sum*10+root.val
                return
            helper(root.left,sum*10+root.val)
            helper(root.right,sum*10+root.val)
        #------------------
        res=[]
        helper(root,0) # subset=[]
        return self.total