class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traversal(root,depth):
            if root==None:
                return
            if len(res)==depth:
                res.append([]) # 1st time when we reach a level we add []
            res[depth].append(root.val)
            traversal(root.left,depth+1)
            traversal(root.right,depth+1)
        #----------------------------------
        res=[]
        traversal(root,0) #depth=0
        return res