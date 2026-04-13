class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        if root.val<val:
            right=self.insertIntoBST(root.right,val)
            root.right=right
        if root.val>val:
            left=self.insertIntoBST(root.left,val)
            root.left=left
        return root