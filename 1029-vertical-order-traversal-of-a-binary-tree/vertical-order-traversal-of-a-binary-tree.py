class Solution:
    def verticalTraversal(self, root):
        def dfs(root,row,col):
            if root==None:
                return
            nodes.append([col,row,root.val])
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)
        #-----------------------------------
        nodes=[]
        dfs(root,0,0)
        nodes.sort()
        #[[-1, 1, 9], [0, 0, 3], [0, 2, 15], [1, 1, 20], [2, 2, 7]]
        res=[]

        prev=None

        for col,row,val in nodes:
            if prev==None or prev!=col:
                res.append([])
            res[-1].append(val)
            prev=col
        return res


        
