class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        res=[]
        q=deque([root])

        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            res.append(max(level))
        return res

