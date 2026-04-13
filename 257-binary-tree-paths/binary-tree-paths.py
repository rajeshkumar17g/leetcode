class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(root,subset):
            if root.left==None and root.right==None:
                res.append("->".join(subset))
                return
                
            if root.left!=None:
                subset.append(str(root.left.val))
                helper(root.left,subset)
                subset.pop()
            
            if root.right!=None:
                subset.append(str(root.right.val))
                helper(root.right,subset)
                subset.pop()
        #------------------------
        res=[]
        helper(root,[str(root.val)])
        return res
