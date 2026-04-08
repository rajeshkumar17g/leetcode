"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children [2,3,4,5]
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traversal(root):
            if root==None:
                return
            
            res.append(root.val)
            for child in root.children: #[10,20,30,40l50]
                traversal(child)
        #---------------------------
        res=[]
        traversal(root)
        return res