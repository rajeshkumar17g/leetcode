class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = None
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            if self.prev and self.prev.val > root.val:
                if self.first==None:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorder(root.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val