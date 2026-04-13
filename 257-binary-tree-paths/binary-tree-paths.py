class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def helper(root,path):
            if root==None:
                return ""
            
            if root.left==None and root.right==None:
                res.append(path+str(root.val))
                return
            helper(root.left,path+str(root.val)+'->')
            helper(root.right,path+str(root.val)+'->')
        #------------------
        res=[]
        helper(root,"") # subset=[]
        return res