class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root):
            if root!=None:
                traversal(root.left)
                traversal(root.right)
                res.append(root.val)
        #------------------------------------
        res=[]
        traversal(root)
        return res