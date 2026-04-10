# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCompleteTree(self, root):
        queue = [root]
        seen_null = False

        while queue:
            node = queue.pop(0)

            if not node:
                seen_null = True
                continue

            if seen_null:
                return False

            queue.append(node.left)
            queue.append(node.right)

        return True