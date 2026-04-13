
class Solution:
    #default arguments subset=[]
    def hasPathSum(self, root: Optional[TreeNode], target: int,subset=[]) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None and sum(subset)+root.val==target:
            return True
        return self.hasPathSum(root.left,target,subset+[root.val]) or self.hasPathSum(root.right,target,subset+[root.val])
