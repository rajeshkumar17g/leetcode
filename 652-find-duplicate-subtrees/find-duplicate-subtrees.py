# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees ={}
        duplicates = []
        def serialize(node):
            if not node:
                return ''
            left = serialize(node.left)
            right = serialize(node.right)

            subtree = f'{node.val},{left},{right}'
            subtrees[subtree] = subtrees.get(subtree, 0) + 1

            if subtrees[subtree] == 2:
                duplicates.append(node)
            return subtree
        serialize(root)
        return duplicates      