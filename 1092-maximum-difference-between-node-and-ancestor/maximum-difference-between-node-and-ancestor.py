# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node,curr_min,curr_max):
            nonlocal ans

            if not node:
                return

            curr_min = min(curr_min,node.val)
            curr_max = max(curr_max,node.val)

            a = abs(node.val - curr_min)
            b = abs(node.val - curr_max)

            ans = max(ans,a,b)

            dfs(node.left,curr_min,curr_max)
            dfs(node.right,curr_min,curr_max)

        dfs(root,root.val,root.val)
        
        return ans