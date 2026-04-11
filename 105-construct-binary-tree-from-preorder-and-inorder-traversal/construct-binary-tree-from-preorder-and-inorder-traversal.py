class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:   
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root