class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def dfs(root,is_left):
            if root==None:
                return
            if root.left==None and root.right==None and is_left==True:
                self.sum=self.sum+root.val
            dfs(root.left,True)
            dfs(root.right,False)
        #--------------------------
        dfs(root,False)
        return self.sum