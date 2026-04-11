class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root,pathsum):
            if root==None:
                return False
            
            current_sum=pathsum+root.val

            if root.left==None and root.right==None:
                return current_sum>=limit
            
            left_sum=dfs(root.left,current_sum)
            right_sum=dfs(root.right,current_sum)

            if left_sum==False:
                root.left=None
            if right_sum==False:
                root.right=None
            
            return left_sum or right_sum
        if dfs(root,0)==True:
            return root
        else:
            return None
