class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        return root