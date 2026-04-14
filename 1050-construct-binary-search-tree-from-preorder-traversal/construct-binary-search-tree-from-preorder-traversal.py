class Solution:
    def bstFromPreorder(self, preorder):
        def construct(bound=float('inf')):
            if not preorder or preorder[0] > bound:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = construct(root.val)
            root.right = construct(bound)
            return root
        return construct()