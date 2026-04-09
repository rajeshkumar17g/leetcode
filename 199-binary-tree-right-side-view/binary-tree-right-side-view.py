class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,depth):
            if root==None: 
                return
            if len(res)==depth: 
                res.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        #-----------------------
        res=[]
        dfs(root,0)
        return res
