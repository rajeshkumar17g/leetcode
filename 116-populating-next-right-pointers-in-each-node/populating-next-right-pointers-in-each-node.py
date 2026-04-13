"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return
        if root.left!=None:
            root.left.next=root.right
        if root.right!=None and root.next!=None:
            root.right.next=root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root