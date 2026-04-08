class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traversal(root):
            if root==None:
                return
            
            for child in root.children:
                traversal(child)
            res.append(root.val)
        #---------------------------
        res=[]
        traversal(root)
        return res