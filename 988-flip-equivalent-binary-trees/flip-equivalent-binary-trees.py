class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None or p.val!=q.val:
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) or (self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left))

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.isSameTree(root1,root2)