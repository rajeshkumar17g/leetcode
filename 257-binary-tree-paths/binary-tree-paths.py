class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, crr):
            if root==None: # crossed leaf node
                return None
            if root.left==None and root.right==None:
                res.append(crr + str(root.val))
                return

            helper(root.left, crr + str(root.val) + "->") 
            helper(root.right, crr + str(root.val) + "->")
        #-----------------------------------------------------------------
        res = []
        helper(root, "")
        return res