# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def dfs(root):
            if root.left==None and root.right==None:
                return "leaf"
            a=None
            b=None
            if root.left!=None:
                a=dfs(root.left)
            if root.right!=None:
                b=dfs(root.right)
            if a=='leaf' or b=='leaf':
                self.count+=1
                return "camera"
            if a=='camera' or b=="camera":
                return "gap"
            if a=="gap" or b=="gap":
                return "leaf"
        if dfs(root)=='leaf':
            return self.count+1
        return self.count