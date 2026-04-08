class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        q=deque([root]) # q=[None] q=[root]. # deque array.  .append(). .popleft()
        res=[]

        while q: # while q is not empty 
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            res.append(level)
        
        return res