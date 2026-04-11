# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        subtrees = []

        def dfs(node):
            nonlocal subtrees

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == x:
                subtrees.append(left)
                subtrees.append(right)
                subtrees.append(n - (left + right + 1))

            return left + right + 1
        
        dfs(root)

        for i in subtrees:
            if i > (n - i):
                return True
        
        return False