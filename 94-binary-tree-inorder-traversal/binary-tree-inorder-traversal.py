class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       stack=[]
       res=[]

       while root!=None or stack!=[]:
            while root!=None: 
                stack.append(root) #save address of last visited node
                root=root.left #move left until left is none
            
            root=stack.pop() # last visited node LIFO
            res.append(root.val)
            root=root.right 
        
       return res