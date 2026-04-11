# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)

        if val>root.val:
            newNode.left = root
            return newNode
        
        curr = root

        while curr.right and curr.right.val>val:
            curr=curr.right
        newNode.left = curr.right
        curr.right = newNode

        return root