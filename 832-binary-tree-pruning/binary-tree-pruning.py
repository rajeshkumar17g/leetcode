class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def traversal(root):
            if root==None:
                return 0
            left_sum=traversal(root.left)
            right_sum=traversal(root.right)
            if left_sum==0:
                root.left=None
            if right_sum==0:
                root.right=None
            if not root.left and not root.right and root.val==0:
                return 0
            return root.val+left_sum+right_sum
            
        #--------------------------------------------
        
        sum=traversal(root)
        if(sum==0):
            return None
        return root
