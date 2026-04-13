
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def dfs(root,res):
            if root==None:
                return
            if root.left==None and root.right==None:
                res.append(root.val)
                return
            dfs(root.left,res)
            dfs(root.right,res)
        #------------------------------
        res1=[]
        res2=[]
        dfs(root1,res1)
        dfs(root2,res2)
        return res1==res2