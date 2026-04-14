# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def make_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = arr[mid]
            root.left = make_tree(left, mid - 1)
            root.right = make_tree(mid + 1, right)

            return root
        def traverse(root):
            if not root:
                return
            else:
                traverse(root.left)
                arr.append(root)
                traverse(root.right)
        arr=[]
        traverse(root)
        return make_tree(0,len(arr)-1)