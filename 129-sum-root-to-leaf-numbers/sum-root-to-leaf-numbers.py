# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,path):
            if root==None:
                return ""
            
            if root.left==None and root.right==None:
                res.append(path+str(root.val))
                return
            helper(root.left,path+str(root.val))
            helper(root.right,path+str(root.val))
        #------------------
        res=[]
        helper(root,"") # subset=[]
        return sum(list(map(int,res)))