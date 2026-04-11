class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def traversal(root):
            if root==None:
                return
            res.add(root.val)
            traversal(root.left)
            traversal(root.right)
        #----------------------
        res=set()
        traversal(root)
        return len(res)==1
        """
        if root==None:
            return True
        if root.left!=None and root.val!=root.left.val:
            return False
        if root.right!=None and root.val!=root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)"""