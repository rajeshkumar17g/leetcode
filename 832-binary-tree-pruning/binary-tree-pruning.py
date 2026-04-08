class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def traversal(root):
            if root==None:
                return None
            root.left = traversal(root.left)
            root.right = traversal(root.right)
            if root.val == 0 and root.left==None and root.right==None:
                return None
            return root
        #----------------------------------------------------------------
        return traversal(root)