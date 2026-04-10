# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root,depth):
            if root==None:
                return
            
            if depth==len(res):
                res.append(root.val)
            
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        #-----------------------------------
        res=[]
        dfs(root,0)
        return res