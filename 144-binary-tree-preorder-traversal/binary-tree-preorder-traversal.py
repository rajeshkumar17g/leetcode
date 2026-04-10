class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root):
            if root==None:
                return
            
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        #---------------------------
        res=[]
        traversal(root)
        return res
"""
       stack=[]
       res=[]

       while root!=None or stack!=[]:
            while root!=None: 
                res.append(root.val)
                stack.append(root) #save address of last visited node
                root=root.left #move left until left is none
            
            root=stack.pop() # last visited node LIFO
            root=root.right 
        
       return res"""