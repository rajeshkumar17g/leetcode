class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        self.curr = dummy
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            root.left = None
            self.curr.right = root
            self.curr = root
            inorder(root.right)
        inorder(root)
        return dummy.right