# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            if root==None:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        #---------------------------------
        res=[]
        inorder(root)
        min=abs(res[1]-res[0])
        for index in range(len(res)-1):
            if res[index+1]-res[index]<min:
                min=res[index+1]-res[index]
        return min